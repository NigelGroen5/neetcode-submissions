class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', '}': '{', ']': '['}

        for i in s:
            
            if i in closeToOpen:
                if stack and closeToOpen[i] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(i)
        
        return not stack
        
