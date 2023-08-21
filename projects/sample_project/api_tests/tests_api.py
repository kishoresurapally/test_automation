import allure

from utils.api import call_api
import allure
from utils.common import global_conf
from utils.json_schema import json_schema_validated
import logging
from pytest import mark
log = logging.getLogger(__name__)

schema = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "array",
    "items": {
        "$ref": "#/definitions/Welcome9Element"
    },
    "definitions": {
        "Welcome9Element": {
            "type": "object",
            "additionalProperties": True,
            "properties": {
                "bookingid": {
                    "type": "integer"
                }
            },
            "required": [
                "bookingid"
            ],
            "title": "Welcome9Element"
        }
    }
}


@mark.smoke
@allure.title("This is sample test title")
@allure.epic("Jira-1")
@allure.link("https://setu.co/")
def test_get_booking_id(config):
    """
    This test validates response of get api and its schema
    """
    endpoint = config.get("url") + "booking"
    response = call_api(endpoint, 'get')
    assert response.status_code
    status = json_schema_validated(response.json(), schema)
    assert status


@mark.Feature1
@allure.severity("NORMAL")
@allure.epic("JIRA-2")
@allure.title("This is sample test title2")
def test_get_booking_id_failure(config):
    """
    This test validates response of get api and its schema
    """
    endpoint = config.get("url") + "booking"
    response = call_api(endpoint, 'get')
    assert response.status_code
    status = json_schema_validated(response.json(), schema)
    assert status is False






