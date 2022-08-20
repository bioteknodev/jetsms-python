# JetSMS 

## Single Sms (1-1) Send

1-1 message send


```python
import os
from client.jetsms import JetSmsSingle

# predefined  JetSms Api url
# JETSMS_URL="https://service.jetsms.com.tr/SMS-Web8/xmlsms"

def sendSingleTest():
	print("Send Single Test")
	jetSmsApiSingle = JetSmsSingle("USERNAME","PASSWORD")
	jetSmsApiSingle.addMessage(gsm="5420000001",text="hello world!")
	smsResult = jetSmsApiSingle.send(title="ORIGINATOR")
	if smsResult.isSend():
		print('sms send')
	else:
		print('sms not send {}'.format(smsResult.toString()))

if __name__ == '__main__':
    sendSingleTest()
```