"""
https://www.onenoughtone.com/learning-path/data-structures-algorithms-patterns/problem/filter-array-by-value

You are given an integer array nums and an integer val. Your task is to eliminate all occurrences of val from the array in-place, meaning you must modify the original array directly without allocating additional space for another array.

The relative order of elements that remain may be changed—what matters is the count and presence of non-matching elements.

Your function should return k, the number of elements in nums that are not equal to val. After your function executes, the first k positions of the array should contain only elements that are not equal to val. The elements beyond index k-1 are irrelevant and can hold any value.

Example 1:
input: nums = [3, 2, 2, 3], val = 3
output: 2

Example 2:
input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
output: 5

Example 3:
input: nums = [1, 2, 3, 4, 5], val = 6
output: 5
"""

class Solution:
    def filter_array(self, nums: list[int], val: int) -> int:
        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left

"""
Time complexity: O(n)
Space complexity: O(1)
"""
