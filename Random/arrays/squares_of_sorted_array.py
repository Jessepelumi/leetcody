# Easy*
# Given an integer array 'nums' sorted in non-decreasing order, return an array of the squares of each number sorted in non-descending order.

def squaresOfSortedArraySort(nums: list[int]) -> list[int]:
    # Square all numbers
    result = []

    for i in nums:
        i **= 2
        result.append(i)

    result.sort() 
    return result
    

# Example usage
arr = [-1,-4,2,10,6]
print(f"Output: {squaresOfSortedArraySort(arr)}")