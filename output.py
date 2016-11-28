#!/usr/bin/python
from abc import ABCMeta, abstractmethod

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
		# Implement me!
		pass