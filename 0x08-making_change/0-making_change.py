#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total.

Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination
of coin in the list
Your solution's runtime will be evaluated in this task
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    coins = sorted(coins)
    count = 0
    while True:
        try:
            max_val = coins[-1]
            total_mode_max = total % max_val
            if total_mode_max == 0:
                count += (total // max_val)
                return count

            for coin in coins:
                if total_mode_max % coin == 0:
                    total_floor_max_val = total // max_val
                    count += total_floor_max_val
                    total = total_mode_max
                    if coin == coins[-2]:
                        count += total // coin
                        return count
                    else:
                        break
            coins = coins[:-1]
        except IndexError:
            return -1
