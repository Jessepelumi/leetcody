class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, v in enumerate(nums):
            comp = target - v

            for comp in seen:
                return [seen[comp], i]
            
            seen[v] = i

# time complexity: O(n)
# space complexity: O(n)
