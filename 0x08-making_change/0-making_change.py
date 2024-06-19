#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins ([List]): [List of Coins available]
        total ([int]): [total amount needed]
    """

    if total == 0:
        return 0

    if total is None:
        return -1

    """ Initialize array (dp table) with "infinity" values."""
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    """ Fill the dp table."""
    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
