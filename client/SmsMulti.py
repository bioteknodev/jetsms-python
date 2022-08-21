import os
from client.SmsResponse import SmsResponse
import urllib2

class SmsMulti:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.list = []

	def addMessage(self,sms):
		self.list.append(sms)

	def send(self,title,url="https://service.jetsms.com.tr/SMS-Web8/xmlsms",startdate="",expiredate=""):
		print(self.list)
		self.data  = '<?xml version="1.0" encoding="utf-8" ?><message-context type="mmmgsd" ><username>'+self.username+'</username><password>'+self.password+'</password><outbox-name>'+title+'</outbox-name><reference></reference><start-date>'+startdate+'</start-date><expire-date>'+expiredate+'</expire-date>'
		for s in self.list:
			self.data += '<message>'
			self.data += '<gsmno>'+s.gsm+'</gsmno>'
			self.data += '<text>'+s.text+'</text>'
			self.data += '</message>'
		self.data += '</message-context>'
		request = urllib2.Request(url, self.data)
		request.add_header('Content-Type', 'text/xml')
		response = urllib2.urlopen(request)
		responseText = response.read()
		return SmsResponse(responseText)