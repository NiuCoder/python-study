# Python支持多种图形界面第三方库，包括：Tk、wxWidgets、Qt、GTK
# Python自带Tk，注意要在有图形界面的系统下使用
from Tkinter import *

class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self,text='Hello,world!')
		self.helloLabel.pack()
		self.quitButton = Button(self,text='Quit',command=self.quit)
		self.quitButton.pack()

app = Application()
app.master.title('Hello,world')
app.mainloop()
