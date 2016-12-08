#!/usr/bin/python

class Player():
	def __init__(self, firstname, lastname, email = None):
		self.firstname = firstname
		self.lastname = lastname
		self.email = email

	def getname(self):
		return self.firstname + " " + self.lastname

	def getfirstname(self):
		return self.firstname

	def getemail(self):
		return self.email

	def tostring(self):
		return self.firstname + " " + self.lastname
	
	def __eq__(self, other):
		if type(other) is type(self):
			return self.__dict__ == other.__dict__
		return False


