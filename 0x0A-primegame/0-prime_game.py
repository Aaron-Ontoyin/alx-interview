#!/usr/bin/python3
"""
Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that number
and its multiples from the set. The player that cannot
make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""


def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determines the winner
    :param x: number of rounds
    :param nums: list of numbers
    :return: name of the winner | None

    Example:

    x = 3, nums = [4, 5, 1]
    First round: 4

    Maria picks 2 and removes 2, 4, leaving 1, 3
    Ben picks 3 and removes 3, leaving 1
    Ben wins because there are no prime numbers left for Maria to choose
    Second round: 5

    Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    Ben picks 3 and removes 3, leaving 1, 5
    Maria picks 5 and removes 5, leaving 1
    Maria wins because there are no prime numbers left for Ben to choose
    Third round: 1

    Ben wins because there are no prime numbers for Maria to choose
    Result: Ben has the most wins
    """
    scores = {"Maria": 0, "Ben": 0}
    for num in nums:
        primes = sorted(
            [i for i in range(2, num + 1) if is_prime(i)], reverse=True
        )
        turn = "Maria"
        while primes:
            for prime in primes:
                primes = [i for i in primes if i % prime != 0]
                if not primes:
                    scores[turn] += 1
                turn = "Ben" if turn == "Maria" else "Maria"
    return max(
        scores,
        key=scores.get
    ) if scores["Maria"] != scores["Ben"] else None
