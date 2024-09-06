#!/usr/bin/python3

"""Making Change
"""


def makeChange(coins, total):
    """Given a list of coins and a total, return the minimum number of coins
    """
    if not coins:
        return -1

    num_coins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        num_coins += total // coin
        total %= coin

    if total == 0:
        return num_coins
    else:
        return -1
