"""
[2,0,2,1,1,0]
 ^
"""

class MultiplePass:
    def tri_value_partition(self, nums: list[int]) -> list[int]:
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

"""
nums = [2,0,2,1,1,0]
=> partitions => [ 0s |  1s  |  Unknown  |  2s  ]
                   ^     ^                  ^
                  low   mid                high
"""

class Solution:
    def tri_value_partition(self, nums: list[int]) -> list[int]:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        return nums

# nums = [2, 0, 2, 1, 1, 0]
# sol = Solution()
# result = sol.tri_value_partition(nums)
# print(result)
