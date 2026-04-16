# Problem: #3 Longest Substring Without Repeating Characters
# Difficulty: Medium

# Sliding window problem

class Solution:
    def longest_substring(self, s: str) -> int:
        seen = set()
        max_window = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            window = right - left + 1
            max_window = max(max_window, window)
            seen.add(s[right])

        return max_window
    
# Time complexity: O(n)
# Space complexity: O(n)


solution = Solution()

s = "abcabcbb"
result = solution.longest_substring(s)
print(result)
