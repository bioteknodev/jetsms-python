import os
from client.response import SmsResponse
import urllib2

class JetSmsSingle:

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def addMessage(self,gsm,text):
		self.gsm = gsm
		self.text = text

	def send(self,title,url="https://service.jetsms.com.tr/SMS-Web8/xmlsms",startdate="",expiredate=""):
		self.data = '<?xml version="1.0" encoding="utf-8" ?><message-context type="smmgsd" ><username>'+self.username+'</username><password>'+self.password+'</password><outbox-name>'+title+'</outbox-name><reference></reference><start-date>'+startdate+'</start-date><expire-date>'+expiredate+'</expire-date><message-header></message-header><text>'+self.text+'</text><gsmnos>'+self.gsm+'</gsmnos></message-context>'
		request = urllib2.Request(url, self.data)
		request.add_header('Content-Type', 'text/xml')
		response = urllib2.urlopen(request)
		responseText = response.read()
		return SmsResponse(responseText)