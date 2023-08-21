"""

API spec validation
<Txn

refCategory=”00|01|02|03|04|05|06|07|08|09
<RiskScores>
<Score provider="sp" type="TXNRISK" value=""/>
<Score provider="NPCI" type="TXNRISK" value=""/>
</RiskScores>
<Rules>
<Rule name="EXPIREAFTER" value="1 miniute to max 64800 minitues"/>
<Rule name="MINAMOUNT" value=""/> </Rules>
</Txn>
"""
from pytest import mark, param


def test_req_auth_details(config):
    """
    1. Test Positive scenario with all cases fields are proper
    """
    pass


def test_head_is_missing(config):
    """
    test request auth details without Head attribute
    """
    pass


def test_ver_is_not_present(config):
    """
    test request auth details without ver attribute
    """
    pass


def test_head_ver_is_1_0(config):
    """
    test request auth details  where ver  is 1.0
    """
    pass


def test_head_ver_is_2_0(config):
    """
    test request auth details  where ver  is 2.0
    """
    pass


def test_head_ver_is_3_0(config):
    """
    test request auth details  where ver  is 3.0
    """
    pass


def test_head_ver_is_blank(config):
    """
    test request auth details  where ver  is blank
    """
    pass


def test_head_ver_is_missing(config):
    """
    test request auth details  where ver  is missing
    """
    pass


def test_head_ts_is_valid_iso_format(config):
    """
    test request auth details  where ts  is valid ISODateTIme
    """
    pass


def test_head_ts_is_invalid_iso_format(config):
    """
    test request auth details where ts  is invalid ISODateTIme
    """
    pass


def test_head_ts_is_utc_format(config):
    """
    test request auth details  where ts  is utc format
    """
    pass


def test_head_ts_is_blank(config):
    """
    test request auth details  where ts is blank
    """
    pass


def test_head_ts_is_missing(config):
    """
    test request auth details  where ts is blank
    """
    pass


def test_head_orig_id_is_of_length_one(config):
    """
    test request auth details  where origId is of length  1
    """
    pass


def test_head_orig_id_is_of_length_twenty(config):
    """
    test request auth details  where origId is of length  20
    """
    pass


def test_head_orig_id_is_of_length_21(config):
    """
    test request auth details  where origId is of length  21
    """
    pass


def test_head_orig_id_is_alphanumeric(config):
    """
    test request auth details  where origId is alphanumeric
    """
    pass


def test_head_orig_id_is_alphanumeric(config):
    """
    test request auth details  where origId is alphanumeric
    """
    pass


def test_head_orig_id_is_missing(config):
    """
    test request auth details  where origId is missing
    """
    pass


def test_head_orig_id_is_blank(config):
    """
    test request auth details  where origId is blank
    """
    pass


def test_head_msg_id_is_of_length_35(config):
    """
    test request auth details  where msgId is of length 35
    """
    pass


def test_head_msg_id_is_of_length_10(config):
    """
    test request auth details  where msgId is of length 10
    """
    pass


def test_head_msg_id_is_numeric(config):
    """
    test request auth details  where msgId is numeric
    """
    pass


def test_head_msg_id_is_more_than_35(config):
    """
    test request auth details  where msgId is of length 36
    """
    pass


def test_head_msg_id_is_blank(config):
    """
    test request auth details  where msgId is blank
    """
    pass


def test_head_msg_id_is_missing(config):
    """
    test request auth details  where msgId is missing
    """
    pass


def test_txn_is_valid(config):
    """
    test request auth details  where txn is valid
    """
    pass


def test_txn_is_missing(config):
    """
    test request auth details  where txn is missing
    """
    pass


def test_txn_id_is_of_length_35(config):
    """
       type: - alphanumeric
       test request auth details  where id is of length 35
    """
    pass


def test_txn_id_is_of_length_10(config):
    """
       type: - alphanumeric
       test request auth details  where id is of length 10
    """
    pass


def test_txn_id_is_of_length_36(config):
    """
       type: - alphanumeric
       test request auth details  where id is of length 36
    """
    pass


def test_txn_id_is_numeric(config):
    """
       type: - alphanumeric
       test request auth details  where txn id is numeric
    """
    pass


def test_txn_id_is_blank(config):
    """
       type: - alphanumeric
       test request auth details  where txn id is blank
    """
    pass


def test_txn_id_is_missing(config):
    """
       type: - alphanumeric
       test request auth details  where txn id is missing
    """
    pass


def test_txn_note_is_of_length_50(config):
    """
       type: - alphanumeric
       test request auth details  where note is of length 50
    """
    pass


def test_txn_note_is_of_length_1(config):
    """
       type: - alphanumeric
       test request auth details  where id note of length 1
    """
    pass


def test_txn_note_is_of_length_51(config):
    """
       type: - alphanumeric
       test request auth details  where note is of length 10
    """
    pass


def test_txn_note_is_numeric(config):
    """
       type: - alphanumeric
       test request auth details  where txn note is numeric
    """
    pass


def test_txn_note_is_blank(config):
    """
       type: - alphanumeric
       test request auth details  where txn note is blank
    """
    pass


def test_txn_note_is_missing(config):
    """
       type: - alphanumeric
       test request auth details  where txn note is missing
    """
    pass


def test_txn_ref_id_is_of_length_35(config):
    """
       type: - alphanumeric
       test request auth details  where refId is of length 35
    """
    pass


def test_txn_ref_id_is_of_length_1(config):
    """
       type: - alphanumeric
       test request auth details  where id refId of length 1
    """
    pass


def test_txn_ref_id_is_of_length_36(config):
    """
       type: - alphanumeric
       test request auth details  where refId is of length 36
    """
    pass


def test_txn_ref_id_is_numeric(config):
    """
       type: - alphanumeric
       test request auth details  where txn refId is numeric
    """
    pass


def test_txn_ref_id_is_blank(config):
    """
       type: - alphanumeric
       test request auth details  where txn refId is blank
    """
    pass


def test_txn_ref_id_is_missing(config):
    """
       type: - alphanumeric
       test request auth details  where txn refId is missing
    """
    pass


def test_txn_ref_url_is_of_length_35(config):
    """
       type: - alphanumeric
       test request auth details  where refUrl is of length 35
    """
    pass


def test_txn_ref_url_is_of_length_1(config):
    """
       type: - alphanumeric
       test request auth details  where id refUrl of length 1
    """
    pass


def test_txn_ref_url_is_of_length_36(config):
    """
       type: - alphanumeric
       test request auth details  where refUrl is of length 36
    """
    pass


def test_txn_ref_url_is_numeric_non_url(config):
    """
       type: - alphanumeric
       test request auth details  where txn refUrl is numeric non url
    """
    pass


def test_txn_ref_url_is_blank(config):
    """
       type: - alphanumeric
       test request auth details  where txn reUrl is blank
    """
    pass


def test_txn_ref_url_is_missing(config):
    """
       type: - alphanumeric
       test request auth details  where txn refUrl is missing
    """
    pass


def test_txn_ts_is_valid_iso_format(config):
    """
    test request auth details  where ts  is valid ISODateTIme
    """
    pass


def test_txn_ts_is_invalid_iso_format(config):
    """
    test request auth details where ts  is invalid ISODateTIme
    """
    pass


def test_txn_ts_is_utc_format(config):
    """
    test request auth details  where ts  is utc format
    """
    pass


def test_txn_ts_is_blank(config):
    """
    test request auth details  where ts is blank
    """
    pass


def test_txn_ts_is_missing(config):
    """
    test request auth details  where ts is blank
    """
    pass


def test_txn_ts_and_head_ts_id_different(config):
    """
    test request auth details  where head ts and txn ts  is valid ISODateTIme and is different.
    """
    pass


def test_txn_type_pay(config):
    """
    test request auth details where type is pay
    """
    pass


def test_txn_type_invalid(config):
    """
    test request auth details where  type is invalid
    """
    pass


def test_txn_type_missing(config):
    """
    test request auth details where  type is missing
    """
    pass


def test_txn_type_blank(config):
    """
    test request auth details where  type is blank
    """
    pass


@mark.parametrize("initiation_mode", ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", ""])
def test_txn_initiation_mode(config):
    """
    test request auth details with all possible combination of initiation mode
    check for condition where initiation mode is 11 and "" and do different operation
    """
    pass


def test_txn_initiation_missing(config):
    """
    test request auth details with all missing initiation mode
    """
    pass


@mark.parametrize("cust_ref", ["804223039157", "9686190945", "", "TestValue", "Test@1234567"])
def test_txn_cust_ref(config):
    """
    possible value is numeric
    test request auth details with all possible combination of custRef
    check for condition where cust ref of length more than 10 and less than 10 also non-Numeric
    """
    pass


def test_txn_cust_ref_missing(config):
    """
     test request auth details with cystRef Missing
    """
    pass


def test_txn_risk_score_missing(config):
    """
     Mandatory - No
     test request auth details with RiskScore is missing,
    """
    pass


def test_txn_risk_score_present(config):
    """
     Mandatory - No
     test request auth details with RiskScore,
    """
    pass


def test_txn_risk_score_with_score_present(config):
    """
     Mandatory - No
     test request auth details with RiskScore
       <Score provider="sp" type="TXNRISK" value=""/>
    """
    pass


def test_txn_risk_score_with_multiple_score_present(config):
    """
     Mandatory - no
     test request auth details with RiskScore
     <Score provider="sp" type="TXNRISK" value=""/>
     <Score provider="NPCI" type="TXNRISK" value=""/>
    """
    pass


def test_txn_risk_score_without_score_present(config):
    """
     Mandatory - no
     test request auth details with RiskScore,
     <RiskScore></RiskScore?
    """
    pass


def test_txn_risk_score_with_multiple_score_present_and_provider_alphanumeric(config):
    """
     Mandatory - yes
     test request auth details with RiskScore
     <Score provider="Test@1234" type="TXNRISK" value="1"/>
     <Score provider="NPCI" type="TXNRISK" value="2"/>
    """
    pass


def test_txn_risk_score_with_multiple_score_present_and_provider_numeric(config):
    """
     Mandatory - yes
     test request auth details with RiskScore
     <Score provider="1234" type="TXNRISK" value="1/>
     <Score provider="NPCI" type="TXNRISK" value="1"/>
    """
    pass


def test_txn_risk_score_with_multiple_score_present_and_provider_blank(config):
    """
     Mandatory - yes
     test request auth details with RiskScore
     <Score provider="" type="TXNRISK" value="1"/>
    """
    pass


def test_txn_risk_score_with_multiple_score_present_and_provider_missing(config):
    """
     Mandatory - yes
     test request auth details with RiskScore
     <Score  type="TXNRISK" value="2"/>
    """
    pass


@mark.parametrize("type", ["TXNRISK", "TEST", ""])
def test_txn_risk_score_with_type(config):
    """
     Mandatory - yes
     test request auth details with RiskScore
     <Score  provider="TEST"  type="TXNRISK" value="2"/>
    """
    pass


def test_txn_risk_score_with_type_missing(config):
    """
     Mandatory - yes
     test request auth details with RiskScore
     <Score  provider="TEST" value="2"/>
    """
    pass


@mark.parametrize("value", [1, 2, 3, 4, 5, 6, ""])
def test_txn_risk_score_with_value(config):
    """
     Mandatory - yes
     test request auth details with RiskScore
     <Score  provider="TEST"  type="TXNRISK" value="2"/>
    """
    pass


def test_txn_risk_score_with_value_missing(config):
    """
     Mandatory - yes
     test request auth details with RiskScore
     <Score  provider="TEST"  type="TXNRISK" />
    """
    pass





