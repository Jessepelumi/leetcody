# Problem: 7. Reverse Integer
# Difficulty: Medium

class Solution:
    def reverse_integer(x: int) -> int:
        INT_MAX = 2**31 - 1

        sign  = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x != 0:
            pop = x % 10
            x = x // 10

            # Check for overflow
            # if result * 10 > INT_MAX return 0
            if result > INT_MAX // 10:
                return 0
            if result == INT_MAX // 10 and pop > 7:
                return 0

            result = (result * 10) + pop

        return result * sign


solution = Solution
x = -231
result = solution.reverse_integer(x)
print(result)
