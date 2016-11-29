#!/usr/bin/python
import os, sys, time
from random import shuffle
from playerinput import CSVPlayerReader
from output import Debug
from model import Player

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

	while True:
		receivers = [x for x in gifters]
		shuffle(receivers)
		if combo_is_valid(gifters, receivers, exclusions):
			break

	playerPairs = [(a,b) for a,b in zip(gifters, receivers)]
	d = Debug()
	d.process(playerPairs)

if __name__ == '__main__':
	main()
