import allure
import pytest
from projects.upi_switch.api.helpers import services
from projects import common
from uuid import uuid4
from  datetime import datetime


@pytest.mark.error
@pytest.mark.payflow
@pytest.mark.certification
@pytest.mark.payeepsp
@allure.id("PE_9")
def test_pay_req_auth_timeout_err(config):
    """
    Details :
    API Involved :  ReqAuthDetail
                     RespAuthDetail
                     ReqTxnConfirmation
                     RespTxnConfirmation
    Type :  Pay
    Approval Type : Non-Pre Approved
    Payer Handle : VPA
    Payee Handle : VPA
    Description : Pay ReqAuth Time out. Error code: U09
    Steps : 1. Payer initiates a Pay Request by entering the Virtual Address of the Payee.
            2.UPI sends ReqAuthDetail to Payee PSP in order to resolve the address
            3. Payee PSP  fails to send RespAuthDetail to UPI within timeout period .
            4.UPI sends response with timeout  error code-U09  to Payer PSP.
            5. UPI sends a ReqTxnConfirmation to Payee PSP with FAILURE message. Payee PSP sends a RespTxnConfirmation
            back to UPI.
    """
    message_id = common.generate_txn_id()
    transaction_id = str(uuid4())
    dict_new = {'ns2:ReqPay': {'Head': {'@msgId': message_id}}
                }

    var = services.request_auth_details(config.get("url"),
                                        transaction_id=transaction_id, payload=dict_new)
    assert var["status_code"] == 200

