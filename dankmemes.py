#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import threading

class DankMemeFrame(Frame):
		def __init__(self, parent):
				Frame.__init__(self, parent, background="white")   
				self.label = Label(self, text="memes", font=("Helvetica", 72*3), anchor=W, justify=LEFT)
				self.parent = parent
				
				self.initUI()

		def initUI(self):
				self.parent.title("DankMemes")
				self.pack(fill=BOTH, expand=1)
				self.label.pack()

		def setPlayer(self, s):
			self.label['text'] = s
			self.label.pack()
			print("emem")


def main():
		root = Tk()
		root.geometry("1920x1080")
		frame = DankMemeFrame(root)
		
		root.after(2000, meme, frame)
		root.mainloop()
		frame.setPlayer("Harambe")



def meme(frame):
	frame.setPlayer("Harambe")

if __name__ == '__main__':
		main()