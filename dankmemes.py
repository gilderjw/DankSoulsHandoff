#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import threading

import time
import os
import pyttsx
import random

def swap(xs, a, b):
    xs[a], xs[b] = xs[b], xs[a]

def permute(xs):
    for a in xrange(len(xs)):
        b = random.choice(xrange(a, len(xs)))
        swap(xs, a, b)

def loop(frame):
	global timeLeft
	global i

	timeLeft = timeLeft - 1

	if timeLeft == 19:
		frame.label['fg'] = "black"


	frame.setTimer(timeLeft)

	if timeLeft == 8:
		i = (i + 1) % len(people)
		if i == 0:
			permute(people)
			print "permuting"
		frame.label['fg'] = "red"
		frame.setPlayer(people[i])
		engine.say(people[i])
		engine.runAndWait()

	if timeLeft < 8 and timeLeft > 0:
		engine.say(timeLeft)
		engine.runAndWait()

	if timeLeft == 0:
		timeLeft = 20
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (.2, 200))
		time.sleep(.2)
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (.2, 200))
		time.sleep(.2)
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (.2, 200))
		time.sleep(.2)
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (.2, 200))
		time.sleep(.2)


		frame.setPlayer(people[i])
		print "donzo"

	print "talking shit"

	frame.after(1000, loop, frame)


class DankMemeFrame(Frame):
		def __init__(self, parent):
				Frame.__init__(self, parent, background="white")   
				self.timerLabel = Label(self, text="memes", font=("Helvetica", 72*3), anchor=W, justify=LEFT)
				self.parent = parent
				self.label = Label(self, text="memes", font=("Helvetica", 72*3), anchor=W, justify=LEFT)
				
				self.initUI()

		def initUI(self):
				self.parent.title("DankMemes")
				self.pack(fill=BOTH, expand=1)
				self.label.pack()
				self.timerLabel.pack()

		def setTimer(self, seconds):
			print "setting timer"
			if(seconds < 30):
				self.timerLabel["fg"] = "red"
			else:
				self.timerLabel["fg"] = "black"

			self.timerLabel["text"] = str(seconds/60) + ":" + str(seconds%60)


		def setPlayer(self, s):
			self.label['text'] = s
			self.label.pack()

engine = pyttsx.init()
engine.setProperty('rate', engine.getProperty('rate'))

frame = None

people = ["John", "Jim", "Andrew", "Chris"]
timeLeft = 20;

for s in people:
	engine.say(s)

engine.runAndWait()

permute(people)
print people

i = 0

def main():
	global frame
	global people

	root = Tk()
	root.geometry("1920x1080")
	frame = DankMemeFrame(root)
	frame.setPlayer(people[i])
	frame.setTimer(20)

	root.after(1000, loop, frame)
	root.mainloop()

if __name__ == '__main__':
		main()