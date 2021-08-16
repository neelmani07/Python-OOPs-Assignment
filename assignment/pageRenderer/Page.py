from Sections import Sections 
class Page:
	def __init__(self,n):
		self.listOfSections=[]
		print('details for page no. %d '%(n+1))
		self.countSections=int(input("no of sections?\n"))
		for i in xrange(self.countSections):
			self.listOfSections.append(Sections(i))
		
	def disp(self):
		for i in xrange(self.countSections):
			print("---------section %d---------"%i)
			self.listOfSections[i].disp()
			print("---------section ends %d---------"%i)
