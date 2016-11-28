#!/usr/bin/python
import os, sys, time
from random import shuffle
from output import Debug
from model import Player

def combo_is_valid(original, permutation, exclusions):
	for i in range(len(original)):
		if original[i] == permutation[i]:
			return False
		else:
			for line in exclusions:
				g, r = line.split()
				if original[i].firstname == g and permutation[i].firstname == r:
					return False
	return True

def main():
	fileInput = [
	"Rozella Westbrooks",
	"Inge Tarwater",
	"Malika Anspach",
	"Tatyana Siu",
	"Gladis Dimaggio",
	"Myrtle Khan",
	"Quinn Lindaeur",
	"Ward Furrow",
	"Rex Sandford",
	"Consuelo Huey",
	"Quincy Torgrimson",
	"Yolande Fregoe"
	]

	exclusionsInput = [
	"Rozella Inge",
	"Ward Rex",
	"Quincy Rozella",
	"Rozella Quincy",
	"Gladis Consuelo"
	]

	gifters = []
	for line in fileInput:
		arr = line.split()
		if len(arr) == 2:
			gifters.append(Player(arr[0], arr[1]))
		elif len(arr) == 3:
			gifters.append(Player(arr[0], arr[1], arr[2]))
		else:
			print "Warning: Skipping '" + line + "'"

	while True:
		receivers = [x for x in gifters]
		shuffle(receivers)
		if combo_is_valid(gifters, receivers, exclusionsInput):
			break

	playerPairs = [(a,b) for a,b in zip(gifters, receivers)]
	d = Debug()
	d.process(playerPairs)

if __name__ == '__main__':
	main()
