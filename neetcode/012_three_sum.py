# Problem: 15. 3Sum
# Difficulty: Medium

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort() # O(n log n) operation

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            # define two pointers
            l, r = i + 1, len(nums) - 1

            while l < r:
                target = nums[i] + nums[l] + nums[r]

                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
                elif target == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return result



solution = Solution()
