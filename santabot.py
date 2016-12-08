#!/usr/bin/python
import os, sys, time
from random import shuffle
from playerinput import CSVPlayerReader
from output import Debug
from output import SMTP
from model import Player

DEBUG_MODE = True

def combo_is_valid(original, permutation, exclusions):
	for i in range(len(original)):
		if original[i] == permutation[i]:
			return False
		else:
			for g, r in exclusions:
				if original[i] == g and permutation[i] == r:
					return False
	return True

def main():
	with open('players.csv') as pfile, open('exclude.csv') as efile:
		reader = CSVPlayerReader(pfile, efile)
	gifters = reader.getPlayers()
	exclusions = reader.getExclusions()

	if DEBUG_MODE:
		print("Loaded " + str(len(gifters)) + " santas and " + (str(len(exclusions))) + " exclusions.")

	combocount = 0
	while True:
		receivers = [x for x in gifters]
		shuffle(receivers)
		combocount += 1
		if combo_is_valid(gifters, receivers, exclusions):
			break
	if DEBUG_MODE:
		print("Found a working combination after " + str(combocount) + " tries.")

	playerPairs = [(a,b) for a,b in zip(gifters, receivers)]
	d = Debug()
	d.process(playerPairs)

	s = SMTP("secretsantasecretservice@gmail.com", "wW7WsWFz1^*1yxjXU2un")
	s.process(playerPairs)


if __name__ == '__main__':
	main()
