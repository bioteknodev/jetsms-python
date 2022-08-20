

class SmsResponse:

	def __init__(self,resultStr):
		resp = resultStr.strip().split(' ')
		self.code = resp.pop(0)
		self.message = ' '.join(resp)

	def isSend(self):
		return self.code == '00'
	
	def toString(self):
		return "{} {}".format(self.code,self.message)
