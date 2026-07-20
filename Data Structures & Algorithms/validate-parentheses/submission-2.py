class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', '}': '{', ']':'['}
        for i in s:
          if i in closeToOpen:
            if stack and stack[-1] == closeToOpen[i]:
              stack.pop(-1)
            else:
              return False
          else:
            stack.append(i)
        if stack:
          return False
        return True