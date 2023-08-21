import requests
import json
import logging as log
from requests import Response


class VaultRepository:
  """ 
  The service for Vault APIs 
  Usage:
    vault_obj = VaultRepository(enabled=Constants.VAULT_ENABLED,
                                role_id=Constants.VAULT_ROLE_ID,
                                secret_id=Constants.VAULT_SECRET_ID,
                                vault_url_prefix=Constants.VAULT_URL_PREFIX,
                                base_url=Constants.VAULT_BASE_URL)
    vault.get_secret("path after vault base url for the data you want to fetch")                            
  """
  def __init__(self, enabled, role_id, secret_id, vault_url_prefix, base_url):
    self.enabled = enabled
    self.role_id = role_id
    self.secret_id = secret_id
    self.vault_url_prefix = vault_url_prefix
    self.base_url = base_url
    self.session = requests.Session()
    self.headers = {"Accept": "application/json", "Content-Type": "application/json"}


  def _validate_response_status(self, response: Response) -> Response:
    """ Check if vault returned a success response """
    parsed_response = response.json()
    if response.status_code != 200:
      log.error(parsed_response)
      raise Exception("Vault did not return a successful response")
    log.debug(parsed_response)
    return response


  def _get_client_token(self):
    """ Get access token """
    if not self.enabled:
      raise Exception("Vault not enabled, can't get access token")
    log.info("Fetching Vault access token...")
    body = json.dumps({
      "role_id": self.role_id,
      "secret_id": self.secret_id,
    })
    resp = self.session.post(self.base_url + "/v1/auth/approle/login", data=body, headers=self.headers)
    resp = self._validate_response_status(resp)
    return resp.json().get("auth", {}).get("client_token")


  def get_secret(self, path: str):
    """ Get secret from given path """
    if not self.enabled:
      raise Exception("Vault not enabled, can't get secrets")
    log.info(f"Fetching secret {path}...")
    full_path = f"{self.vault_url_prefix}{path}"
    headers = {"X-Vault-Token": self._get_client_token()}
    resp = self.session.get(self.base_url + full_path, headers={**self.headers, **headers})
    resp = self._validate_response_status(resp)
    return resp.json()
    