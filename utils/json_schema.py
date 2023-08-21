"""JSON and JSON schema validation functions"""

import json
import logging

from jsonschema import validate, ValidationError

log = logging.getLogger(__name__)


def dict_to_json_string(dictionary):
    json_string = None
    try:
        json_string = json.dumps(dictionary)
        log.debug(f"  json_String is {json_string}")
    except TypeError:
        log.exception("dict_to_json_string failed with error: \n{}".format(dictionary))
    return json_string


def json_string_to_dict(json_string):
    response_dict = None
    try:
        response_dict = json.loads(json_string.decode('utf-8'))
    except ValueError:
        log.exception("json_string_to_dict failed with error: \n{}".format(json_string))
    return response_dict


def json_schema_validated(response_dict, json_schema):
    try:
        validate(response_dict, json_schema)
        log.info("JSON schema validation successful")
        return True
    except ValidationError as err:
        log.exception("json_schema_validated failed with error: \n{}".format(err))
    return False

# TODO: Validate jsonschema using swagger
