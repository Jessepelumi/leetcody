class Solution:
    def longestSubstring(self, s: str) -> int:
        seen = set()
        max_window = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            window = (r - l) + 1
            max_window = max(max_window, window)

            seen.add(s[r])

        return max_window
