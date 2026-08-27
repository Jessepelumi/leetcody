"""
Important cues:
1. In-place modification
2. Non-zero element: elements greater or less than zero
3. Preserve the order in which the non-zero elements appear

Variables:
write - points to the position to write a non-zero value to
read - iterates through the array

Algorithm
1. Iterate through the array using read
2. Swap elements where the value at write is 0 and the value at read is not zero,
    then move the write pointer
3. Move the write pointer whenever the value at right is non-zero
4. Return the modified array
"""

class Solution:
    def relocate_zeroes(self, nums: list[int]) -> list[int]:
        write = 0

        for read in range(len(nums)):
            if nums[write] == 0 and nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            elif nums[write] != 0:
                write += 1

        return nums
