# will check payload type details from swagger

response_pay_payload = f'''<upi:RespPay xmlns:upi="http://npci.org/upi/schema">
        <Head msgId="BOIa4097f0d7c684ca4a6e2eddc965968b1" orgId="410005" ts="2018-02-17T13:39:56.040+05:30" ver="2.0">
        </Head>
        <Resp actn="string" errCode="" reqMsgId="1GRDpegBbA5wfscXLm20" result="SUCCESS">
            <Ref IFSC="string" acNum="string" accType="string" addr="laxmi@boi" approvalNum="959826" code="string" 
            orgAmount="string" respCode="00" reversalRespCode="string" seqNum="1" settAmount="100" 
            settCurrency="INR" type="PAYEE">
            </Ref>
        </Resp>
        <RiskScores>
            <Score type="NPCI" provider="TXNRISK" value="00995">
            </Score>
        </RiskScores>
        <Txn custRef="804813039157" id="AXIb1fbc9cea1f34049904e083034723d49" initiationMode="00" note="testpay" orgRespCode="string" 
        orgRrn="string" orgTxnDate="string" orgTxnId="string" purpose="string" refCategory="string" refId="804813039157"
         refUrl="http://axis.com/upi" subType="PAY" ts="2018-02-17T13:39:54.944+05:30" type="CREDIT">
        </Txn>
        </upi:RespPay>'''

request_pay_payload_collect = f'''
<ns2:ReqPay xmlns:ns2="http://npci.org/upi/schema/">
    <Head msgId="AXI4e11325e968340fba48ebe70cb6be409" orgId="400000" ts="2018-02-23T14:52:32.422+05:30" ver="2.0"/>
    <Txn custRef="805414040578" id="AXIfcd764aeab2a4bd195b25d652c1887f7" initiationMode="00" note="collect" refId="805414040578" refUrl="http://axis.com/upi" ts="2018-02-23T14:52:32.427+05:30" type="COLLECT">
        <Rules>
            <Rule name="EXPIREAFTER" value="1440"/>
            <Rule name="MINAMOUNT" value="1.00"/>
        </Rules>
    </Txn>
    <Payer addr="shyam@boi" code="0000" name="shyam" seqNum="1" type="PERSON">
        <Amount curr="INR" value="2.00"/>
    </Payer>
    <Payees>
        <Payee addr="ram@axis" code="0000" name="RAM" seqNum="1" type="PERSON">
            <Info>
                <Identity id="058010100083492" type="ACCOUNT" verifiedName="Ram"/>
                <Rating verifiedAddress="TRUE"/>
            </Info>
            <Device>
                <Tag name="MOBILE" value="918143308193"/>
                <Tag name="GEOCODE" value="72.991948,19.174975"/>
                <Tag name="ID" value="911489204188596"/>
                <Tag name="OS" value="Android5.1"/>
                <Tag name="IP" value="10.33.237.58"/>
                <Tag name="APP" value="com.upi.axispay"/>
                <Tag name="TYPE" value="MOB"/>
                <Tag name="CAPABILITY" value="011001"/>
            </Device>
            <Ac addrType="ACCOUNT">
                <Detail name="ACTYPE" value="SAVINGS"/>
                <Detail name="ACNUM" value="058010100083000"/>
                <Detail name="IFSC" value="AXIS0000058"/>
            </Ac>
            <Amount curr="INR" value="2.00"/>
        </Payee>
    </Payees>
</ns2:ReqPay>
'''

req_auth_details = '''
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ns2:ReqAuthDetails xmlns:ns2="http://npci.org/upi/schema/" xmlns:ns3="http://npci.org/cm/schema/">
    <Head ver="2.0" ts="2022-02-23T15:05:12+05:30" orgId="NPCI" msgId="PT89501325899164040308004"/>
    <Txn id="3ff615f6-8571-46ee-a21f-0b941247b48e" note="testpay" refId="804813039157" refUrl="http://axis.com/upi" ts="2022-02-23T15:05:12+05:30" type="PAY" custRef="804813039157" initiationMode="00">
        <RiskScores/>
    </Txn>
    <Payees>
        <Payee addr="deku@mha" seqNum="1" type="PERSON">
            <Amount value="2.00" curr="INR"/>
        </Payee>
    </Payees>
    <Payer addr="ram@axis" name="RAM" seqNum="1" type="PERSON" code="0000">
        <Info>
            <Identity id="2345678765" type="ACCOUNT" verifiedName="RAM" id="058010100083492"/>
            <Rating verifiedAddress="TRUE">
            </Rating>
        </Info>
        <Ac addrType="ACCOUNT">
            <Detail name="ACTYPE" value="SAVINGS"/>
            <Detail name="ACNUM" value="058010100083000"/>
            <Detail name="IFSC" value="AXIS0000058"/>
        </Ac>
        <Amount value="2.00" curr="INR"/>
    </Payer>
</ns2:ReqAuthDetails>
'''