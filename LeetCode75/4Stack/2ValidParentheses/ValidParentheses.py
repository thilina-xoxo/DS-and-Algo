class Solution:

    def isValid(self, s:str) -> bool:

        stack = []
        paran = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in paran:
                if stack and stack[-1] == paran[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack


sol = Solution()

s1 = "()[]{}"
s2 = "(]"

print(sol.isValid(s1))
print(sol.isValid(s2))