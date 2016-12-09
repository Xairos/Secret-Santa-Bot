# Secret Santa Bot

Secret Santa is a gift-exchanging game ([Wikipedia Link](https://en.wikipedia.org/wiki/Secret_Santa)) where each player is assigned another player to anonymously give a gift to. Picking names out of a hat can get repetetive when someone picks themselves by chance, and selection needs to restart.

Secret Santa Bot picks a winning combination in one fell swoop, and prints the results! Additionally, enable email output to send players their assigned recipient discretely. 

## Usage

The bot runs with Python 2.7 using only built-in libraries.

Add participants to `players.csv`, and optionally, exclusions to `exclude.csv`.  
Then, just let SantaBot do its thing:
```
~$ python santabot.py
```
And that's it! Enjoy.