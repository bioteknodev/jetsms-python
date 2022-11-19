# JetSMS

USERNAME= JetSMS customer user username

PASSWORD= JetSMS customer user password

ORIGINATOR= JetSMS customer approved originator


## Single Sms (1-1) send

```python
import os
from client.SmsSingle import SmsSingle

# predefined  JetSms Api url
# JETSMS_URL="https://service.jetsms.com.tr/SMS-Web8/xmlsms"

def sendSingleTest():
	print("Send Single Test")
	jetSmsApiSingle = SmsSingle("USERNAME","PASSWORD")
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
from client.SmsMulti import SmsMulti
from client.SmsMessage import SmsMessage

# predefined  JetSms Api url
# JETSMS_URL="https://service.jetsms.com.tr/SMS-Web8/xmlsms"

def sendMultipleTest():
	jetSmsApiMulti = SmsMulti("USERNAME","PASSWORD")
	jetSmsApiMulti.addMessage(sms=SmsMessage(gsm='5420000001',text='hello 001'))
	jetSmsApiMulti.addMessage(sms=SmsMessage(gsm='5420000002',text='hello 002'))
	smsResult = jetSmsApiMulti.send(title="ORIGINATOR")
	if smsResult.isSend():
		print('sms send')
	else:
		print('sms not send {}'.format(smsResult.toString()))


if __name__ == '__main__':
    sendMultipleTest()
```
