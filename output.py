#!/usr/bin/python
from abc import ABCMeta, abstractmethod
import smtplib

class Output:
	__metaclass__ = ABCMeta

	@abstractmethod
	def process(self, playerPairs):
		pass

class Debug(Output):
	def process(self, playerPairs):
		for gifter,receiver in playerPairs:
			print gifter.tostring() + " --> " + receiver.tostring()

class SMTP(Output):
	def __init__(self, email, password):
		self.email = email
		self.password = password

	def process(self, playerPairs):
		subject = "It\'s beginning to feel a lot like Christmas!"
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(self.email, self.password)
		for gifter,receiver in playerPairs:
			if ((gifter.getemail() == None) or (gifter.getemail() == "None")):
				print("WARN: No email listed for " + gifter.getname())
				continue
			content = "\r\n".join([
  				"From: " + self.email,
  				"To: " + gifter.getemail(),
  				"Subject: " + subject,
  				"",
  				"Hey " + gifter.getfirstname() + ", it\'s that time of year again!",
				"",
				"You are " + receiver.getname() + "\'s secret santa!",
				"",
				"Good luck and Happy Holidays!",
				"Santa\'s Secret Santa Secret Service (S.S.S.S.S)"
  			])
			server.sendmail(self.email, gifter.getemail(), content)
		server.quit()
