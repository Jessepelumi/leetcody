# Problem: #1 Two Sum
# Difficulty: Easy

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, value in enumerate(nums):
            comp = target - value

            if comp in seen:
                return [seen[comp], index]
            
            seen[value] = index

# Time complexity: O(n)
# Space complexity: O(n)


solution = Solution()

nums = [11, 21, 31, -41]
target = -30
result = solution.two_sum(nums, target)
print(result)
