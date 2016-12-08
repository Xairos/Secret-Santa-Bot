#!/usr/bin/python
import csv
from abc import ABCMeta, abstractmethod
from model import Player

class PlayerReader:
	__metaclass__ = ABCMeta

	@abstractmethod
	def getPlayers(self):
		pass
	@abstractmethod
	def getExclusions(self):
		pass

class CSVPlayerReader(PlayerReader):
	def __init__(self, playerFile, exclusionFile):
		self.playerFile = playerFile
		self.exclusionFile = exclusionFile

		players = []
		exclusions = []

		# First name, Last name, Gender, Email
		for row in csv.reader(self.playerFile):
			assert len(row) == 3
			players.append(Player(*row))

		# Firstname lastname, Firstname lastname
		for row in csv.reader(self.exclusionFile):
			assert len(row) == 2
			g, r = row
			# Verify players
			gifterExclusion = (x for x in players if x.getname() == g).next()
			receiverExclusion = (x for x in players if x.getname() == r).next()
			
			exclusions.append((gifterExclusion, receiverExclusion))
		self.players = players
		self.exclusions = exclusions

	def getPlayers(self):
		return self.players

	def getExclusions(self):
		return self.exclusions
