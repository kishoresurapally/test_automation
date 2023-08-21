import pytest
import allure
from projects.upi_switch.api.helpers import services
from projects.upi_switch.common import get_csv


@allure.epic("UPI 1.0 SPEC")
def test_req_pay():
    """
    A Pay scenario where Payer is using VPA with remitter details as A/C + IFSC & Payee is VPA .
    FRM Success case(response code -00)
    """
    pass


@allure.epic("UPI 1.0 SPEC")
@pytest.mark.smoke
@pytest.mark.RespPay
@pytest.mark.api
@allure.severity(allure.severity_level.BLOCKER)
def test_res_pay(config):
    """
    Test to validate response api for all valid parameter
    """
    var = services.response_pay_api(config.get("url"),
                                    transaction_id="12345667890")
    assert var["status_code"] == 200


@allure.epic("UPI 1.0 SPEC")
@pytest.mark.smoke
@pytest.mark.RespPay
@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
def test_res_pay_small_message_id(config):
    """
    Test to validate response api for all valid parameter with varying values
    """
    dict_new = {'upi:RespPay': {'Head':
                {'@msgId': "BOIa4097", "@orgId": "410405"},
                'Resp': {"Ref":
                             {'@IFSC': "CITI000006", "@acNum": "5029168816"}}}}

    var = services.response_pay_api(config.get("url"),
                                    transaction_id="12345667890", payload=dict_new)
    assert var["status_code"] == 200


@allure.epic("UPI 1.0 SPEC")
@pytest.mark.destructive
@pytest.mark.RespPay
@pytest.mark.api
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize("msg_id", get_csv("dataset.csv"))
def test_fuzz_response_pay_msg_id(msg_id, config):
    """
    This test intention is to fuzz the RespPayAPI msgID with multiple values.
    """
    dict_new = {'upi:RespPay': {'Head':
                {'@msgId': f"{msg_id[1]}"}}}

    var = services.response_pay_api(config.get("url"),
                                    transaction_id="12345667890", payload=dict_new)
    assert var["status_code"] == 200


@allure.epic("UPI 1.0 SPEC")
@pytest.mark.destructive
@pytest.mark.RespPay
@pytest.mark.api
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize("orig_id", get_csv("dataset.csv"))
def test_fuzz_response_pay(orig_id, config):
    """
    This test intention is to fuzz the RespPayAPI msgID with multiple values.
    """
    dict_new = {'upi:RespPay': {'Head':
                {'@msgId': f"{orig_id[2]}"}}}

    var = services.response_pay_api(config.get("url"),
                                    transaction_id="34234234223432423423", payload=dict_new)
    assert var["status_code"] == 200


@allure.epic("UPI 1.0 SPEC")
@pytest.mark.smoke
@pytest.mark.collect
@pytest.mark.api
@allure.severity(allure.severity_level.BLOCKER)
def test_req_pay(config):
    """
    Test to validate response api for all valid parameter
    """
    var = services.request_pay_api(config.get("url"))
    assert var["status_code"] == 200