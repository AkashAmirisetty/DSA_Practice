# Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid and return true if the string is balanced otherwise return false.


# Examples:
# Input: str = “()[{}()]”

# Output: True

# Explanation: As every open bracket has its corresponding close bracket. Match parentheses are in correct order hence they are balanced.
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Solution:
    def isValid(self, str: str) -> bool:
        stack=[]
        n=len(str)
        for i in range(n):
            if (str[i]=='(' or str[i]=='[' or str[i]=='{'):
                stack.append(str[i])
            else:
                if not stack:
                    return False
                top=stack.pop()
                if ((str[i]==')' and top=='(') or (str[i]==']' and top=='[') or (str[i]=='}' and top=='{')):
                    pass
                else:
                    return False
        return len(stack)==0



    