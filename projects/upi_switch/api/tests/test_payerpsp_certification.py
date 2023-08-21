import allure
import pytest


@pytest.mark.smoke
@pytest.mark.payflow
@pytest.mark.certification
@pytest.mark.payerpsp
@allure.id("PR_4")
def test_payer_vpa_payee_vpa():
    """
     "A Pay scenario where Payer is using VPA with remitter details as A/C + IFSC & Payee is financial address .
      FRM Success case(response code -00)"
    """
    pass
