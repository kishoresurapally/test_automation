"""API related functions"""

import logging

import requests
from allure import step

log = logging.getLogger(__name__)


@step
def call_api(url, method='get', payload=None, headers=None):
    request = getattr(requests, method.lower())
    log.info('* Request URL: %s' % url)
    log.info('* Request method: %s' % method)
    if payload:
        log.debug('* Request payload: %s' % payload)
    if headers:
        log.debug('* Request headers: %s' % headers)

    try:
        response = request(url, headers=headers, data=payload, verify=False, timeout=60)
        log.debug("Response Headers : " + str(response.headers))
        log.debug("Response Code    : " + str(response.status_code))
        log.debug('Response: \n%s' % response.text)
    except Exception as e:
        log.exception('Call API failed: %s' % e)
        return None
    return response


def json_api(url, method='get', payload=None, headers=None):
    headers = headers or {}
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    return call_api(url, method, payload, headers)


def xml_api(url, method='get', payload=None, headers=None):
    headers = headers or {}
    headers["Accept"] = "application/xml"
    headers["Content-Type"] = "application/xml"
    return call_api(url, method, payload, headers)
