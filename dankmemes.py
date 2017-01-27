#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import threading

import time
import os
import pyttsx
import random

engine = pyttsx.init()

def swap(xs, a, b):
    xs[a], xs[b] = xs[b], xs[a]

def permute(xs):
    for a in xrange(len(xs)):
        b = random.choice(xrange(a, len(xs)))
        swap(xs, a, b)

people = ["John", "Jim", "Andrew", "Chris"]


for s in people:
	engine.say(s)

engine.runAndWait()

permute(people)
print people

i = 0

def loop(frame):
	global i
	global people

	engine.say("Next Is " + people[i])
	frame.label['text']=people[i]
	engine.runAndWait()

	engine.say("7")
	engine.say("6")
	engine.say("5")
	engine.say("4")
	engine.say("3")
	engine.say("2")
	engine.say("1")
	engine.runAndWait()
	time.sleep(1)
	i = (i + 1) % len(people)

	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (.2, 200))
	time.sleep(.2)
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (.2, 200))
	time.sleep(.2)
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (.2, 200))
	time.sleep(.2)
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (.2, 200))
	time.sleep(.2)

	if i == 0:
		permute(people)
		print "permuting"

	frame.after(2000, loop, frame)


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
		
		root.after(2000, loop, frame)
		root.mainloop()

if __name__ == '__main__':
		main()