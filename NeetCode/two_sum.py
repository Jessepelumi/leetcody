"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

"""
My solution:
Target is the sum of exactly two elements of the array -> x + y = target
When the value of x is known, y can be found by subtracting x from target -> target - x = y

- Loop through the nums array to obtain a possible value for x and subtract from target
- Compare the result of the initial subtraction with the remaining elements of num to obtain the possible value for y
- Ensure the same index is not repeated
- Return the indices of x and y

- To have access to and store indices, use enumerate instead of range.
"""

def two_sum(nums: list, target: int) -> list:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i


# Usage
nums = [2,7,11,15]
target = 9

print(two_sum(nums, target))
