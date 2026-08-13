"""
Link: https://www.onenoughtone.com/learning-path/data-structures-algorithms-patterns/problem/inplace-unique-elements

You are given an integer array values that is pre-sorted in ascending order (non-decreasing sequence). Your task is to eliminate all duplicate occurrences directly within the array, ensuring that each distinct value appears exactly once. The elements must maintain their original relative ordering after the removal process.

Since modifying the array length is not possible in some programming languages, you must perform this transformation in-place. The unique elements should be placed at the beginning of the array, and you must return the count k representing the number of unique elements.

After your function executes, the first k positions of the array should hold all unique values in sorted order. The values remaining beyond index k-1 are irrelevant and can be ignored by the evaluator.

Example 1:
input: values = [1, 1, 2]
output: k = 2, values = [1, 2, _]

Example 2:
input: values = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
output: k = 2, values = [0, 1, 2, 3, 4, _, _, _, _, _]

Example 3:
input: values = [1, 2, 3, 4, 5]
output: k = 5, values = [1, 2, 3, 4, 5]
"""

class Solution:
    def return_unique_elements(self, values: list[int]) -> int:
        left = 0

        for right in range(1, len(values)):
            if values[right] != values[left]:
                left += 1
                values[left] = values[right]

        return left + 1

"""
Time complexity: O(n)
Space complexity: O(1)
"""
