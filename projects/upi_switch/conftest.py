import pytest
from pytest import fixture
import os
import json
import logging as log
import utils.common as common


def pytest_html_report_title(report):
    report.title = "UPI Switch Test Report"


@fixture(scope='session')
def read_config(config):
    config_file = "config.json"
    try:
        cur_path = os.path.abspath(os.path.dirname(__file__))
        file = os.path.join(cur_path, config_file)
        log.debug(f"file path : {file}")
        log.debug("config.json file: {}".format(file))
        with open(file) as fp:
            common.config = json.load(fp).get('all')
        yield config
    except Exception as e:
        log.error("Failed to load config.json due to: {}".format(str(e)))


@fixture(scope='session')
def get_driver(browser: object):
    driver = browser
    yield driver

