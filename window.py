#!/usr/bin/env python

from tkinter import *
import math


class cook:
	

	def equals_ozgram(self):
		ounce = 0
		try:
			ounce = float(self.e.get())
			ml = 28.34
			self.value = ounce * ml
		except SyntaxError or NameError:
			self.e.delete(0, END)
			self.e.insert(0, 'Invalid Input')
		else:
			self.e.delete(0, END)
			self.e.insert(0, self.value)
	
	def equals_ozml(self):
		ounce = 0
		try:
			ounce = float(self.e.get())
			ml = 28.41
			self.value = ounce * ml
		except SyntaxError or NameError:
			self.e.delete(0, END)
			self.e.insert(0, 'Invalid Input')
		else:
			self.e.delete(0, END)
			self.e.insert(0, self.value)
		

	def action(self,argi): 

		self.e.insert(END,argi)

	def clearall(self): 
		"""when clear button is pressed,clears the text input area"""
		self.e.delete(0,END)
	
	def clear1(self):
		self.txt=self.e.get()[:-1]
		self.e.delete(0,END)
		self.e.insert(0,self.txt)

	def __init__(self, master):

		master.title('cooking unit converter')
		master.geometry()
		self.e= Entry(master)
		self.e.grid(row=0 ,column =0, columnspan=3, pady= 3)
		self.e.focus_set()
		self.div='÷'
		#self.newdiv=self.div.decode('utf-8')
		
		Button(master, text="OZ to gram", width = 10, command= lambda:self.equals_ozgram()).grid(row =8, column=1)
		Button(master, text="OZ to ml", width = 10, command= lambda:self.equals_ozml()).grid(row =10, column=1)
		#Button(master, text="OZ to gram", width = 10, command= lambda:self.equals()).grid(row =3, column=1)
		Button(master,text='AC',width=3,command=lambda:self.clearall()).grid(row=1, column=6)
		Button(master,text='C',width=3,command=lambda:self.clear1()).grid(row=2, column=6)
		Button(master,text="7",width=3,command=lambda:self.action(7)).grid(row=1, column=0)
		Button(master,text="8",width=3,command=lambda:self.action(8)).grid(row=1, column=1)
		Button(master,text="9",width=3,command=lambda:self.action(9)).grid(row=1, column=2)
		Button(master,text="4",width=3,command=lambda:self.action(4)).grid(row=2, column=0)
		Button(master,text="5",width=3,command=lambda:self.action(5)).grid(row=2, column=1)
		Button(master,text="6",width=3,command=lambda:self.action(6)).grid(row=2, column=2)
		Button(master,text="1",width=3,command=lambda:self.action(1)).grid(row=3, column=0)
		Button(master,text="2",width=3,command=lambda:self.action(2)).grid(row=3, column=1)
		Button(master,text="3",width=3,command=lambda:self.action(3)).grid(row=3, column=2)
		Button(master,text="0",width=3,command=lambda:self.action(0)).grid(row=4, column=0)
		Button(master,text=".",width=3,command=lambda:self.action('.')).grid(row=4, column=1)



root = Tk()
obj = cook(root)
root.mainloop()


#create oz to ml method
# create oz to gram method
