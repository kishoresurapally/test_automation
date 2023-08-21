import json
from datetime import datetime
import os

import allure
import pytest
import logging
from utils import common
from utils.browser import web_driver_launch
log = logging.getLogger(__name__)

# global fixtures only, please don't add project related code here

driver = None


@pytest.fixture(scope='session', autouse=True)
def config(request):
    """"Loads config.json to common.config once before the test session starts"""
    env = (request.config.getoption("--env")).lower()
    try:
        config_file = "config.json"
        cur_path = os.path.abspath(os.path.dirname(__file__))
        for root, dirs, files in os.walk(cur_path):
            for name in files:
                if name == config_file:
                    match = root

        file = os.path.join(match, config_file)
        log.debug("config.json file: {}".format(file))
        with open(file) as fp:
            config = json.load(fp).get(env)
            #TODO: implement for all
            common.global_conf = config
        yield config
    except Exception as e:
        log.error("Failed to load config.json due to: {}".format(str(e)))


@pytest.fixture(scope='function', autouse=True)
def log_test_state(request):
    """"Logs test name at the start and end of each test"""
    log.info("Test '{}' STARTED\n".format(request.node.nodeid))
    yield
    log.info("Test '{}' COMPLETED\n".format(request.node.nodeid))


# Browser related fixtures
@pytest.fixture(scope="session")
def browser(request):
    """  Starts and stops web driver instance once per session
    to start chrome, firefox, IE etc."""
    global driver
    browser_driver = (request.config.getoption("--browser_driver")).lower()
    browser = (request.config.getoption("--browser")).lower()
    driver = web_driver_launch(browser)
    yield driver
    log.debug('Quitting driver instance')
    driver.quit()
    driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """Capture browser screenshot on error and embed in html report"""
    outcome = yield
    report = outcome.get_result()
    summary = []
    extra = getattr(report, "extra", [])
    xfail = hasattr(report, "wasxfail")
    setattr(report, "duration_formatter", "%H:%M:%S.%f")
    failure = (report.skipped and xfail) or (report.failed and not xfail)
    capture_debug = failure
    if capture_debug and driver is not None:
        _gather_url(item, summary, extra)
        _gather_screenshot(item, summary, extra)
        _gather_html(item, summary, extra)
        _gather_logs(item, summary, extra)
    if summary:
        report.sections.append(("selenium", "\n".join(summary)))
    report.extra = extra


def _gather_url(item, summary, extra):
    try:
        url = driver.current_url
    except Exception as e:
        summary.append("WARNING: Failed to gather URL: {0}".format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin("html")
    if pytest_html is not None:
        # add url to the html report
        extra.append(pytest_html.extras.url(url))

    summary.append("URL: {0}".format(url))
    allure.attach(url, attachment_type=allure.attachment_type.URI_LIST)


def _gather_screenshot(item, summary, extra):
    try:
        screenshot = driver.get_screenshot_as_base64()
        screenshot_png = driver.get_screenshot_as_png()
    except Exception as e:
        summary.append("WARNING: Failed to gather screenshot: {0}".format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin("html")
    if pytest_html is not None:
        # add screenshot to the html report
        extra.append(pytest_html.extras.image(screenshot, "Screenshot"))
    allure.attach(screenshot_png, attachment_type=allure.attachment_type.PNG)


def _gather_html(item, summary, extra):
    try:
        html = driver.page_source
    except Exception as e:
        summary.append("WARNING: Failed to gather HTML: {0}".format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin("html")
    if pytest_html is not None:
        # add page source to the html report
        extra.append(pytest_html.extras.text(html, "HTML"))
    allure.attach(html, attachment_type=allure.attachment_type.TEXT)


def _gather_logs(item, summary, extra):
    pytest_html = item.config.pluginmanager.getplugin("html")
    try:
        types = driver.log_types
    except Exception as e:
        # note that some drivers may not implement log types
        summary.append("WARNING: Failed to gather log types: {0}".format(e))
        return
    for name in types:
        try:
            browser_log = driver.get_log(name)
        except Exception as e:
            summary.append("WARNING: Failed to gather {0} log: {1}".format(name, e))
            return
        if pytest_html is not None:
            extra.append(
                pytest_html.extras.text(format_log(browser_log), "%s Log" % name.title())
            )
        allure.attach(format_log(browser_log), attachment_type=allure.attachment_type.TEXT)


def format_log(logged_items):
    timestamp_format = "%Y-%m-%d %H:%M:%S.%f"
    entries = [
        u"{0} {1[level]} - {1[message]}".format(
            datetime.utcfromtimestamp(entry["timestamp"] / 1000.0).strftime(
                timestamp_format
            ),
            entry,
        ).rstrip()
        for entry in logged_items
    ]
    logged_items = "\n".join(entries)
    return logged_items


def pytest_addoption(parser):
    """Command line arguments"""
    parser.addoption(
        "--env", action="store", default="qa_env", help="Environment selection"
    )
    parser.addoption(
        "--browser_driver", action="store", default="selenium", help="driver selection , eg. selenium, playwright"
    )
    parser.addoption(
        "--browser", action="store", default="chrome", help="webdriver selection"
    )
    parser.addoption(
        "--ip", action="store", default="127.0.0.1", help="remote ip"
    )


#TODO : jira commit linking
#TODO : Bdd implemetaion  - UAT
#TODO : performance Testing options   -for mixed api flow
#TOD0 : Production env simulation usig

