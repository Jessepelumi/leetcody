"""
Important cues:
1. Positive integers
2. The difference between two positions determines the width of the container
3. The shorter value of the pair determines the height of the container

Variables:
left - starts from the beginning of the array
right - starts from the end of the array
    Together, the form a pair and the sides of the container
max_capacity - holds the maximum capacity of the container

Algorithm:
1. Loop through the array from both ends using the left and right pointers, as long as right is greater than left
2. Compute distance and area (capacity of the container)
3. Move the left pointer if it holds the lesser value of the pair, if not move the right pointer.
"""

class Solution:
    def maximum_water(self, height: list[int]):
        left = 0
        right = len(height) - 1
        max_capacity = 0

        while left < right:
            capacity = min(height[left], height[right]) * (right - left)
            max_capacity = max(capacity, max_capacity)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_capacity
            
