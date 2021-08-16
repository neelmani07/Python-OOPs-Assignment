from Components import Components
class Sections:
	typesOfComp="Heading , Sub-Heading , Image , Icons , Links , Body"
	def __init__(self,no):
		self.listOfComp=[]
		print("details for section no.%d"%(no+1))
		self.countComp=int(input("no of components?\n"))
		print("choose from %s \n"%self.typesOfComp)
		for i in xrange(self.countComp):
			
			typeOf=input("\nComponent type?")
			style=input("style?")
			val=input("value?")
			self.listOfComp.append(Components(typeOf,style,val))
			
	def disp(self):
		for i in self.listOfComp:
			i.disp()
