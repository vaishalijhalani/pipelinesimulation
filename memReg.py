

class RegClass:
	def __init__(self,num):
		self.reg_dict = dict()		
		for i in range(num):
			self.reg_dict['$t'+str(i)] = None
