class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in seen:
                return [comp[seen], i]

            seen[comp] = i

# time complexity: O(n)
# space complexity: O(n)
