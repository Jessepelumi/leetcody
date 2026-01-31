"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

"""
My solution:

- Convert the elements of the array to a string using the join statement
- Then do a type conversion to an integer and increment
- Type convert to a string again and put into an array. 
NOTE: This solution works but it is not what the problem requires, because the given integer is a LARGE integer.

- Loop through digits backwards 
- Check if the last digit is less than 9, if it is, increment by 1
"""

def plusOne(digits: list) -> list:
    for i in range(len(digits) - 1, -1, -1):
        # check if the last digit is less than 9
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            pass

# Usage
digits = [1, 2, 3, 4, 5]
print(plusOne(digits))