# JetSMS

USERNAME= JetSMS customer user username
PASSWORD= JetSMS customer user password
ORIGINATOR= JetSMS customer approved originator

## Single Sms (1-1) send

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

## Multiple Sms (n-n) send

```python
import os
from client.multiple import JetSmsMulti
from client.sms import JetSmsSMS

# predefined  JetSms Api url
# JETSMS_URL="https://service.jetsms.com.tr/SMS-Web8/xmlsms"

def sendMultipleTest():
	jetSmsApiMulti = JetSmsMulti("USERNAME","PASSWORD")
	jetSmsApiMulti.addMessage(sms=JetSmsSMS(gsm='5420000001',text='hello 001'))
	jetSmsApiMulti.addMessage(sms=JetSmsSMS(gsm='5420000002',text='hello 002'))
	smsResult = jetSmsApiMulti.send(title="ORIGINATOR")
	if smsResult.isSend():
		print('sms send')
	else:
		print('sms not send {}'.format(smsResult.toString()))


if __name__ == '__main__':
    sendMultipleTest()
```
