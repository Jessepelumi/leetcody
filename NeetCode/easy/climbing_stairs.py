"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""

"""
My solution:

Identify the sequence of steps:
From the example, ways(1) = 1 and ways(3) = 3.
For when n is 2: ways(2) = 2.
For when n is 4: ways(4) = 5
Sequence so far -> 1, 2, 3, 5.

Identified formula:
ways(3) = ways(2) + ways(1)
ways(4) = ways(3) + ways(2)
Then, ways(n) = ways(n - 1) + ways(n - 2) (Recursive formula)

This problem can then be solved recursively. 
"""

def climbing_stairs(n: int) -> int:
    # base case
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbing_stairs(n - 1) + climbing_stairs(n - 2) # recursive formula
    # time complexity -> O(2^n) -> this follows O(branch^n)
    # space complexity -> O(n)
