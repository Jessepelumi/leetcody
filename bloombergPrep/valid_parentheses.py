"""
String, Stack
Bloomberg Easy
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if len(stack) == 0:
                    return False
                
                pop_val = stack.pop()
                if bracket_map[char] != pop_val:
                    return False
                
        if len(stack) != 0:
            return False
        
        return True
