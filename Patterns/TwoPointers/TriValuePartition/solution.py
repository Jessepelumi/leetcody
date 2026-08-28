"""
[2,0,2,1,1,0]
 ^
"""

class MultiplePass:
    def tri_value_partition(nums: list[int]) -> list[int]:
        count_zero = 0
        count_one = 0
        count_two = 0

        for num in nums:
            if num == 0:
                count_zero += 1
            elif num == 1:
                count_one += 1
            else:
                count_two += 1

        for i in range(count_zero):
            nums[i] = 0
        for i in range(count_zero, count_zero + count_one):
            nums[i] = 1
        for i in range(count_zero + count_one, len(nums)):
            nums[i] = 2

        return nums 
