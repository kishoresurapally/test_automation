"""Api Service definition which includes methods , schema validation and payload and api path"""
import logging
import collections
import allure
import xmltodict
from utils.api import xml_api
import projects.upi_switch.api.helpers.payload as default_payload

log = logging.getLogger(__name__)


def xml_to_dict(updated_payload):
    """
    This function converts xml to dictionary
    """
    xml_dict = xmltodict.parse(updated_payload)
    return xml_dict


def dict_xml(payload):
    """
    This Function converts dict to xml
    """
    updated_payload = xmltodict.unparse(payload)
    return updated_payload


@allure.step
def update_xml(updated_payload, value_to_update):
    """ This function takes values that need to be updated in the given xml files"""
    xml_converted_to_dict = xml_to_dict(updated_payload)
    updated_dictionary = update(xml_converted_to_dict, value_to_update)
    modified_xml = dict_xml(updated_dictionary)
    return modified_xml


def update(actual_dict, value_to_update):
    """
    This Function update Dictionary with new values provided in other dictionary
    """
    for key, value in value_to_update.items():
        if isinstance(value, collections.abc.Mapping):
            actual_dict[key] = update(actual_dict.get(key, {}), value)
        else:
            actual_dict[key] = value
    return actual_dict


@allure.step
def response_pay_api(url, transaction_id, payload=None):
    """
    Response API URL RespPay UPI - Detail Definition can be found in spec document
    """
    log.debug(f"Inside Response pay : Response pay TransactionId: {transaction_id}")
    updated_payload = default_payload.response_pay_payload
    if payload:
        updated_payload = update_xml(updated_payload, payload)
    endpoint = f"{url}upi/RespPay/2.0/{transaction_id}"
    var = xml_api(endpoint, "post", updated_payload)
    log.debug(f"Values for response pay API is 'status_code': {var.status_code},\n  'content': {var.content}")
    return {"status_code": var.status_code, "content": var.content}


@allure.step
def request_pay_api(url, payload=None):
    """
    Response API URL RespPay UPI - Detail Definition can be found in spec document
    """
    updated_payload = default_payload.request_pay_payload_collect
    if payload:
        updated_payload = update_xml(updated_payload, payload)
    endpoint = f"{url}upi/collect"
    var = xml_api(endpoint, "post", updated_payload)
    log.debug(f"Values for request pay collect API is 'status_code': {var.status_code},\n  'content': {var.content}")
    return {"status_code": var.status_code, "content": var.content}


@allure.step
def request_auth_details(url, transaction_id, payload=None):
    """
    Response API URL RespPay UPI - Detail Definition can be found in spec document
    """
    updated_payload = default_payload.request_pay_payload_collect
    if payload:
        updated_payload = update_xml(updated_payload, payload)
    endpoint = f"{url}upi/ReqAuthDetails/2.0/urn:txnid:" + transaction_id
    var = xml_api(endpoint, "post", updated_payload)
    log.debug(f"Values for request auth details API is 'status_code': {var.status_code},\n  'content': {var.content}")
    return {"status_code": var.status_code, "content": var.content}

