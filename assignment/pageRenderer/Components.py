class Components:
	def __init__(self, typeOf, value, style):
		self.value=value
		self.typeOf=typeOf
		self.style=style
	
	def disp(self):
		print(self.typeOf)
		print('\n')
		print("\tvalue=%s"%self.value)
		print('\n')
		print("\tstyle=%s"%self.style)
		print('\n')
