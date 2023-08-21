# UPI Switch Tests

This Repo Deals with Functional test requirement

## Build Plan

## Build Status

## Security

## Documentation

## Third Party Components

- Allure , Junit 

## PyTest Documentation

##### Table of Contents

1. [Overview](#overview)
2. [Quick start](#quick)
3. [Project structure](#structure)
4. [Grouping tests](#markers)
5. [How to run tests](#tests)

<a name="overview"></a>

## Overview

## Advantages

- Simple and easy to understand
- Common codebase for across projects
- Plug and play using open source plugins
- Allow tests to be executed in parallel
- Rich analysis and debugging features using HTML reports and Dashboards
- Templates available for faster on-boarding of a new products
- Supports custom markers & test types for grouping tests. E.g. UI, API, Smoke, Sanity, BVT etc.
- Auto re-run failed tests

<a name="quick"></a>

## Quick start

```
# clone repo
repo details will cohe here
 
cd test_automatiom
 
# install virtualenv module
pip install virtualenv
 
# create a new virtual environment
python -m venv venv

# activate virtual environment

# on Windows
venv\Scripts\activate.bat

# on Linux and MacOS
source venv/bin/activate
 
# install project requirements
pip install -r requirements.txt
 
# verify pytest is installed
pytest -h
```

<a name="structure"></a>

## Project structure

- `projects`  all python code, tests under product/module/tests folder
- `results`  test reports, execution logs etc. would be generated here
- `config.json`  json based configurations for test setup, metadata, execution, reporting etc.
- `utils`  utility functions not related to DCF for tests, rest, browser, jira, json, assertion etc
- `helpers`  product related utility functions 
-
- `conftest.py`  global fixtures to manage execution of tests, setup, cleanup & other common fixtures
- `pytest.ini` pytest configurations and can be overridden by command line arguments

<a name="markers"></a>

## Grouping of tests

Tests can be grouped based on markers, which could be any string. E.g. Smoke, BVT, API, UI etc. Note: all markers must
be defined in [pytest.ini](pytest.ini), when --strict-markers flag enabled.

### marking a test method

```
@pytest.mark.sanity
@pytest.mark.api
def test_get_request():
    pass
```

### multiple markers for the whole file

```
import pytest
pytestmark = [pytest.mark.ui, pytest.mark.sanity]
```

### multiple markers for a class

```
import pytest
class TestClass:
    pytestmark = [pytest.mark.ui, pytest.mark.regression]
```

Below are the registered markers in [pytest.ini](pytest.ini)

###### Register a new marker in [pytest.ini](pytest.ini) before using it, else pytest will fail due to default `--strict-markers` flag.

```
    smoke:                  Smoke, Sanity, BVT tests
    api:                    API tests
    browser:                Browser based tests
    desktop:                Desktop app tests
```

<a name="tests"></a>

## How to execute tests

```
# All tests under sample_project, using relative path of a test folder
$ pytest projects/sample_project

# All api tests under sample_project
$ pytest projects/sample_project/api
$ pytest projects/sample_project/api/tests

# All smoke tests under sample_project, using smoke marker
$ pytest -m smoke projects/sample_project

# All API smoke tests under sample_project, using api folder and smoke marker
$ pytest -m smoke projects/sample_project/api

# All smoke tests in a file, using a filename and smoke marker
$ pytest -m smoke projects/sample_project/api/test_api.py

# A single test, using test name as keyword
$ pytest -k 'test_method_name'
$ pytest -k 'test_method_name' projects/sample_project

# All tests in a class, using class name as keyword
$ pytest -k 'test_class_name'
$ pytest -k 'test_class_name' projects/sample_project (folder name)

# All sanity tests, except in api/dir1 and dir2 folders
$ pytest -m sanity -k "not (api/dir1 and dir2)"

# All tests, filtered by allure epics, features and stories markers
$ pytest --allure-stories story_1,story_2
$ pytest --allure-features feature2 --allure-epics epic3

# All tests, filtered by allure severity markers
$ pytest --allure-severities normal,critical
```


## Test Parallelization

Tests can run concurrently using Jenkins, PyTest or any other mechanism.

- Jenkins: tests can be segregated via markers, folders or test files and run via concurrent Jenkins builds. E.g. UI and
  API tests could be run in parallel.
- PyTest: use below command line parameters. E.g. `--workers 4` will execute 4 concurrent tests in 4 separate processes.

```
  --workers (string):           Set the max num of workers (aka processes) to start (int or "auto" for one per core)
  --tests_per_worker (string):  Set the max num of concurrent tests for each worker (int or "auto" for split evenly)
```

## Headless UI support

Running UI tests in headless manner make them faster and less error-prone. Currently, only Chrome and Firefox support
headless mode, IE will be supported soon. To enable headless browsers, set headless=true as an environment variable. It
gets ignored, if Chrome or Firefox not used.

```
export headless=true
```

## Selenium proxy

To enable selenium proxy, set selenium_proxy=value as an environment variable. On linux, use below bash command:

```
export selenium_proxy=127.0.0.1:8080
```

Using a proxy while running selenium tests is highly beneficial. E.g.

- Burp suite to record the network traffic and use functional automation for network and vulnerability scans
- JMeter or Postman to record API tests from functional automation for faster test scripting

## Automation best practices

Please refer to below pages:

To be added

## Design diagram

To be added

## Sample tests



## Tutorials



## Requirements

Python dependencies in [requirements.txt](requirements.txt):

## Learning resources

- `python`  [**interactive tutorial**](https://learnpython.org)
- `python`  [**interactive tutorial**](https://www.programiz.com/python-programming)
- `pytest`  [**Examples**](https://docs.pytest.org/en/latest/example/index.html)
