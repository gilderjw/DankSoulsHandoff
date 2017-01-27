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
		engine.say(" ")
		engine.say(" ")
		engine.say(" ")
		engine.say(" ")

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

	frame.after(1000, loop, frame)

def incrementDeath(name, dType):
	global deaths
	global frame

	deaths[name][dType] = deaths[name][dType] + 1
	# print deaths
	frame.refreshDeaths(people[i])

class DankMemeFrame(Frame):
		def __init__(self, parent):
				Frame.__init__(self, parent, background="white")   
				self.timerLabel = Label(self, bg="white",text="memes", font=("Helvetica", 72*3), anchor=W, justify=LEFT)
				self.parent = parent
				self.label = Label(self, text="memes", bg="white", font=("Helvetica", 72*3), anchor=W, justify=LEFT)
				self.deaths = Label(self, bg="white",text="normal=\npendulum=\ntrap=\n", font=("Helvetica", 36), justify=LEFT)
				self.normalButton = Button(self, text="normal", command=lambda: incrementDeath(people[i],"normal"))
				self.pendulumButton = Button(self, text="pendulum", command=lambda: incrementDeath(people[i],"pendulum"))
				self.trapButton = Button(self, text="trap", command=lambda: incrementDeath(people[i],"trap"))
				self.initUI()

		def initUI(self):
				self.parent.title("DankMemes")
				self.pack(fill=BOTH, expand=1)
				self.label.pack()
				self.normalButton.pack()
				self.pendulumButton.pack()
				self.trapButton.pack()

				self.timerLabel.pack()
				self.deaths.place(x=5,y=5)

		def setTimer(self, seconds):
			print "setting timer"
			if(seconds < 30):
				self.timerLabel["fg"] = "red"
			else:
				self.timerLabel["fg"] = "black"

			self.timerLabel["text"] = str(seconds/60) + ":" + "{:0>2}".format(seconds%60)

		def refreshDeaths(self,s):
			global deaths
			string = ""
			print deaths
			for k in deaths[s]:
				string = k + ": " + str(deaths[s][k]) + '\n' + string

			self.deaths['text'] = string

		def setPlayer(self, s):
			self.label['text'] = s
			self.label.pack()
			self.refreshDeaths(s)

engine = pyttsx.init()
engine.setProperty('rate', engine.getProperty('rate'))

frame = None

people = ["John", "Jim", "Andrew", "Chris"]

deaths = {}
bosses = {}

for person in people:
	deaths[person] = {"normal": 0, "pendulum": 0, "trap": 0}

for person in people:
	bosses[person] = []

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
	global deaths

	root = Tk()
	root.geometry("1920x1080")
	frame = DankMemeFrame(root)
	frame.setPlayer(people[i])
	frame.setTimer(20)

	root.after(1000, loop, frame)
	root.mainloop()



if __name__ == '__main__':
		main()