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


def check_prime(n):
    """Check if number is prime"""
    return all([(n % j) for j in range(2, int(n**0.5) + 1)]) and n > 1


def remove_multiples(n, num_list):
    """Remove multiples of n from num_list"""
    return [num for num in num_list if num % n != 0]


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
    for game_round in range(x):
        num_list = list(range(1, nums[game_round] + 1))
        turn = 0
        while num_list:
            num_list = sorted(
                [num for num in num_list if check_prime(num)], reverse=True
            )
            if num_list:
                num_list = remove_multiples(num_list[0], num_list)
                turn += 1
        scores["Maria" if turn % 2 != 0 else "Ben"] += 1
    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    elif scores["Maria"] < scores["Ben"]:
        return "Ben"
    else:
        return None
