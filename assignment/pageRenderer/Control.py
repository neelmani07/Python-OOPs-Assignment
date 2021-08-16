from Page import Page 
class Control:
	def Menu(self):
		
		while True:
			print("In Menu \n 1)create Page\t2)display Page\t3)end program")
			self.arg=input()
			if self.arg==1:
				self.createPage()
			elif self.arg==2:
				self.dispPage()
			elif self.arg==3:
				self.end()
			else:
				print("put from 1,2,3")
	def end(self):
		exit()
	def createPage(self):
			self.pageList.append(Page(self.num))
			self.num+=1
	def dispPage(self):
		pageNo=input("enter the page no to display\n")
		self.pageList[pageNo-1].disp()
	def __init__(self):
		self.num=0
		#self.pageCount=input("enter the no of pages")
		self.pageList=[]
		self.Menu()
		
obj=Control()

	
