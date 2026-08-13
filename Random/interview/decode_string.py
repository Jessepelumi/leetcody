"""
String, Stack
Bloomberg Medium
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        current_str = ""
        current_num = 0

        for char in s:
            # Check and build number
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            # Check open bracket and append to stack
            if char == "[":
                stack.append((current_str, current_num))

                current_str = ""
                current_num = 0

            # Check closing bracket and pop from stack
            if char == "]":
                prev, num = stack.pop()

                current_str = prev + num * current_str

            # when a letter comes after a letter
            else:
                current_str += char

        return current_str
