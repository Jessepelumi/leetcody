"""
Important cues:
1. Non-decreasing order (ascending order)
2. In-place modification (don't create another array)
3. k is the valid and important part of the array

Variables:
1. read - iterates through the array
2. write - points to a position where a valid value can be placed
3. count - keeps track of the number of times a value has been seen
4. previous - helps determine when a new value begins

Algorithm:
1. Iterate through the array
2. Check if current == previous:
    - If they are the same, increment count
    - If not, set previous = current to begin a new count
3. If count <= 2, set the value of the write position to current
4. Return write
"""

class Solution:
    def limit_occurences(self, nums: list) -> int:
        write = 0
        count = 0
        previous = None

        for read in range(len(nums)):
            current = nums[read]

            if current == previous:
                count += 1
            else:
                previous = current
                count = 1

            if count <= 2:
                nums[write] = current
                write += 1

        return write
