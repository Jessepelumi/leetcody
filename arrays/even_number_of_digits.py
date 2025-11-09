# Easy*
# Given an array 'nums', return how many of them contain an even number of digits.

"""
Loop through the array and convert each number to string, then check if the lenght of the resulting string is even.
When the check results to an even number, increment count, and return it when the loop stops.
"""

def evenNumberOfDigits(nums: list[int]) -> int:
    count = 0

    for i in nums:
        i = str(i)

        if len(i) % 2 == 0:
            count += 1

    return count



# Runtime complexities
# Time -> O(n)
# Space -> O(1)

# Example usage
arr = [12,345,2,6,7896]
print(f"Output: {evenNumberOfDigits(arr)}")