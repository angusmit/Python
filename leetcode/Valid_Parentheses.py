#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

#solution
class Solution:
    def isValid(self, s: str) -> bool:
        h = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                h.append(s[i])
            elif s[i] == ")" and len(h) != 0 and h[-1] == "(":
                h.pop()
            elif s[i] == "]" and len(h) != 0 and h[-1] == "[":
                h.pop()
            elif s[i] == "}" and len(h) != 0 and h[-1] == "{":
                h.pop()
            else:
                return False
        return not h