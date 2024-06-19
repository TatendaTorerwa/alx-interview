# 0x08. Making Change

## Description

This project involves solving the classic coin change problem using Python. The goal is to determine the fewest number of coins needed to meet a given total amount using a list of coin denominations. This problem is a common example in dynamic programming and greedy algorithms, and it tests algorithmic efficiency and correctness.

## Concepts Covered

- **Greedy Algorithms**:
  - Understanding the working of greedy algorithms.
  - Recognizing their limitations and scenarios where they might not provide the optimal solution.

- **Dynamic Programming**:
  - Principles of dynamic programming.
  - Overlapping subproblems and optimal substructure.
  - Iterative and recursive approaches.

- **Algorithmic Complexity**:
  - Analyzing time and space complexity.
  - Striving for efficient solutions.

- **Problem-Solving Strategies**:
  - Breaking down problems into manageable sub-problems.
  - Iterative vs. recursive dynamic programming approaches.

- **Python Programming**:
  - Manipulating lists and using list comprehensions.
  - Implementing functions with efficient loops and conditional statements.

## Resources

- **Python Official Documentation**:
  - [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (for loops, if statements)
  
- **GeeksforGeeks Articles**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
  
- **YouTube Tutorials**:
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=Y0ZqKpToTic) for a visual and step-by-step explanation of the dynamic programming approach.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Task

### 0. Change comes from within

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- **Prototype**: `def makeChange(coins, total)`
- **Return**: fewest number of coins needed to meet total
- If total is 0 or less, return 0
- If total cannot be met by any number of coins you have, return -1
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list

### Example

```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Expected output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1

