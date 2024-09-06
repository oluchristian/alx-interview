#!/usr/bin/python3
"""Prime Game: Maria and Ben are playing a game"""


def isWinner(rounds, nums):
    """Determines the winner of the game."""
    if rounds <= 0 or nums is None or rounds != len(nums):
        return None

    ben_wins = 0
    maria_wins = 0

    primes = [1] * (max(nums) + 1)
    primes[0], primes[1] = 0, 0

    for i in range(2, len(primes)):
        remove_multiples(primes, i)

    for num in nums:
        if sum(primes[:num + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None


def remove_multiples(lst, x):
    """Removes multiples of primes."""
    for i in range(2, len(lst)):
        try:
            lst[i * x] = 0
        except IndexError:
            break
