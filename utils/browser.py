"""Browser based functions via Selenium WebDriver"""

import logging
import os
from time import sleep

from allure import step
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

log = logging.getLogger(__name__)


@step
def type_text(browser, locator, text):
    element = get_element(browser, locator)
    move_to_element(browser, element)
    element.clear()
    sleep(1)
    return element.send_keys(text)


@step
def send_keystrokes(browser, locator, text):
    element = get_element(browser, locator)
    for character in text:
        element.send_keys(character)
        sleep(0.15)


@step
def is_displayed(browser, locator):
    try:
        get_element(browser, locator, 10).is_displayed()
    except TimeoutException:
        return False
    return True


@step
def is_text_present(browser, text):
    return text in browser.page_source


def get_element(browser, locator, timeout=30):
    return WebDriverWait(browser, timeout).until(expected_conditions.element_to_be_clickable((By.XPATH, locator)))


def load_time(browser, timeout):
    return browser.set_page_load_timeout(timeout)


@step
def click_element(browser, locator):
    element = get_element(browser, locator)
    move_to_element(browser, element)
    return element.click()


@step
def main_window(browser):
    browser.close()
    handles = browser.window_handles
    browser.switch_to.window(handles[0])


def move_to_element(browser, element):
    actions = ActionChains(browser)
    actions.move_to_element(element).perform()


def get_text(browser, locator):
    return get_element(browser, locator).text


def explicit_wait(browser, expected_condition, timeout=20):
    return WebDriverWait(browser, timeout).until(expected_condition)


@step
def web_driver_launch(browser):
    driver = None
    assert browser in ["firefox", "chrome", "ie"], f"Unsupported browser: {browser}"
    if browser == "firefox":
        driver = get_firefox_driver()
    elif browser == "chrome":
        driver = get_chrome_driver()
    elif browser == "ie":
        driver = get_ie_driver()
    driver.implicitly_wait(60)
    driver.maximize_window()
    return driver


def get_ie_driver():
    options = webdriver.IeOptions()
    options.add_argument("--window-size=1920,1080")
    options.ignore_protected_mode_settings = True
    capability = webdriver.DesiredCapabilities.INTERNETEXPLORER
    capability['acceptSslCerts'] = True
    headless = os.getenv("headless")
    if headless:
        log.debug(f"Headless mode on IE not supported:")
    proxy = os.getenv("selenium_proxy")
    if proxy is not None:
        capability["proxy"] = {
            "proxyType": "manual",
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy,
        }
    driver = webdriver.Ie(IEDriverManager().install(), options=options, desired_capabilities=capability)
    log.debug("New IE driver instance created")
    return driver


def get_firefox_driver():
    options = webdriver.FirefoxOptions()
    options.set_preference("accept_untrusted_certs", True)
    options.set_preference("assume_untrusted_cert_issuer", True)
    capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
    capabilities['acceptInsecureCerts'] = True
    headless = os.getenv("headless")
    if headless:
        log.debug(f"Firefox headless mode enabled: {headless}")
        options.add_argument("--headless")
    proxy = os.getenv("selenium_proxy")
    if proxy is not None:
        log.debug("Firefox proxy enabled")
        capabilities["marionette"] = True
        capabilities["proxy"] = {
            "proxyType": "MANUAL",
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy
        }
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                               firefox_options=options, desired_capabilities=capabilities)
    log.debug("New Firefox driver instance created")
    return driver


def get_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("w3c", True)
    options.accept_untrusted_certs = True
    options.assume_untrusted_cert_issuer = True
    options.add_argument("--ignore-certificate-errors")
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    logger.setLevel(logging.WARNING)  # or any variant from ERROR, CRITICAL or NOTSET
    headless = os.getenv("headless")
    proxy = os.getenv("selenium_proxy")
    if headless:
        log.debug(f"Chrome headless mode enabled: {headless}")
        options.headless = True
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
    if proxy is not None:
        log.debug(f"Chrome proxy enabled: {proxy}")
        options.add_argument(f"--proxy-server={proxy}")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    log.debug("New Chrome driver instance created")
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver
