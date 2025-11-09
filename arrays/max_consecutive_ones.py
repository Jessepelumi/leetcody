# Easy*
# Given a binary array 'nums', return the maximum number of consecutive 1s in the array. 

"""
To find the maximum number of consecutive 1s, track when the counting of 1s begin and when it breaks using a 'count' variable. Encountering a 0 indicates the end of a counting set, then reset 'count'.
The highest value of 'count' should be stored in 'max_count' and returned.
The value of 'max_count' is the maximum number of consecutive 1s.
"""

def max_consecutive_ones(arr: list[int]) -> int:
    count = 0
    max_count = 0

    for i in arr:
        if i == 1:
            count += 1
        else:
            max_count = max(max_count, count)   # Set max_count to the highest value between max_count and count
            count = 0   # Reset the count to begin counting new set of 1s

    max_count = max(max_count, count)
    return max_count



# Runtime complexities 
# Time complexity -> O(n)
# Space complexity -> O(1)

# Example cases
arr = [1,1,0,1,1,1]
print(f"Output: {max_consecutive_ones(arr)}")