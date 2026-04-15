# Problem: 5. Longest Palindromic Substring
# Difficulty: Medium

class Solution:
    def longest_palindrome(s: str) -> str:
        # Find the center and expand
        # Odd center -> (i, i)
        # Even center -> (i, i + 1)

        longest = ""

        # Helper function for expansion
        def expand(left: int, right: int):
            # For expansion to happen,
            # Index must be within the bounds of the string,
            # And the value must be equal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        for i in range(len(s)):
            p1 = expand(i, i) # Odd expansion
            p2 = expand(i, i+1) # Even expansion

            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2

        return longest
    
# Time complexity: O(n^2)
# Space complexity: O(1)
    
solution = Solution
s = "babad"
result = solution.longest_palindrome(s)
print(result)
