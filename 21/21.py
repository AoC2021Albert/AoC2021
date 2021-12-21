#!/usr/bin/env python
#
# $ ./21.py 4 8
# 444356092776315
# $ ./21.py 10 8
# 221109915584112
#
# Note: part 1 done on Google Sheets
# https://docs.google.com/spreadsheets/d/16AoFTAcY7zIsJXEe56ZGJ7X8kORFvsvX2B07vCGtCzA/edit?usp=sharing

from collections import defaultdict
import sys

THREEDICECOMBOS = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]
# example: THREEDICECOMBOS[4] == 3 because there are 3 ways to get a 4
# There is no way to get 0, 1 or 2, the maximum you can get is threedicecomobs[9] == 1
MINTHREEDICE = 3
MAXTHREEDICE = 9

WINNING_SCORE = 21
MAXTHROWS = WINNING_SCORE  # (each throw adds a minimum of 1 point)
# (we can get a 20 and +9 on the next, beyond that we do not care)
MAXPOINTS = WINNING_SCORE + 9
MAXCELLS = 10


def get_win_lose(startspace):
    # We will return an array where each position represents the number of throws
    # Inside there will be a tuple of ("winning universes","losing universes")
    win_lose = [(0, 0)] * MAXTHROWS

    # tps[throws][points][space]=combinations
    tps = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    # Note: I could avoid the top level dictionary as I only care about the current round and the next
    # but this makes the code somewhat easier to understand IMO

    # We fill throw by throw
    # We start with the initial position
    # The only combination here is 0 throws, 0 points, startpos, 1 universe/combination
    tps[0][0][startspace] = 1

    for current_throw in range(MAXTHROWS):
        prev_round = tps[current_throw]
        next_round = tps[current_throw+1]
        for starting_points in prev_round.keys():
            if starting_points < WINNING_SCORE:  # We do not want combinations after winning
                for starting_space in prev_round[starting_points].keys():
                    for threediceresult in range(MINTHREEDICE, MAXTHREEDICE + 1):
                        next_space = starting_space + threediceresult
                        if next_space > 10:
                            next_space -= 10
                        next_points = starting_points + next_space
                        next_round[next_points][next_space] += prev_round[starting_points][starting_space] * \
                            THREEDICECOMBOS[threediceresult]

        # next_round is now completed
        # Now compute winning universes and losing universes for this amount of throws
        winning = 0
        losing = 0
        for starting_points in next_round.keys():
            total_universes = sum(
                combos for combos in next_round[starting_points].values())
            if starting_points >= WINNING_SCORE:
                winning += total_universes
            else:
                losing += total_universes
        win_lose[current_throw] = (winning, losing)
    return(win_lose)


player1 = get_win_lose(int(sys.argv[1]))
player2 = get_win_lose(int(sys.argv[2]))

player1winuniverses = sum(player1[round][0] * player2[round-1][1]
                          for round in range(1, MAXTHROWS))
player2winuniverses = sum(player2[round][0] * player1[round][1]
                          for round in range(1, MAXTHROWS))

print(max(player1winuniverses, player2winuniverses))
