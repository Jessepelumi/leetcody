"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
"""

"""
My solution:

- Ensure the lenght of s is even
- Keep track of all opening brackets using a stack 
- The most recent opening bracket must match the most recent closing bracket
- No closing bracket must be encountered while the stack is empty
- After processing the entire string, the stack must be empty
"""

def valid_parentheses(s: str) -> bool:
    # check if the length of s is even
    if len(s) % 2 != 0:
        return False
    
    stack = []
    pairs = {")":"(", "]":"[", "}":"{"}

    for bracket in s:
        if bracket in pairs.values():
            stack.append(bracket)
        elif bracket in pairs:
            if not stack:
                return False
            
            pop_val = stack.pop()
            if pop_val != pairs[bracket]:
                return False
            
    if len(stack) != 0:
        return False
    
    return True

# time complexity -> O(n)
# space complexity -> O(n)

# Usage
s = "(("
print(valid_parentheses(s))


# my brute-force solution
# def valid_parentheses(s: str) -> bool:
#     stack = []

#     # check if length of s is even
#     if len(s) % 2 != 0: return False

#     for _, bracket in enumerate(s):
#         if bracket == "(" or bracket == "[" or bracket == "{":
#             stack.append(bracket)
#         elif bracket == ")":
#             if len(stack) == 0: return False
#             result = stack.pop()
#             if result != "(": return False
#         elif bracket == "]":
#             if len(stack) == 0: return False
#             result = stack.pop()
#             if result != "[": return False
#         elif bracket == "}":
#             if len(stack) == 0: return False
#             result = stack.pop()
#             if result != "{": return False

#     if len(stack) != 0: return False

#     return True
