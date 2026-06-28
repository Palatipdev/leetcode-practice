class Solution:
    def isValid(self, s: str) -> bool:
        # [{()}] o: [ , {  ,(  c: ), }, ]
        openList = ["[","{","("]
        closeList = ["]","}",")"]
        stack = []
        i = 0

        while i < len(s):
            if s[i] in openList:
                stack.append(s[i])
                i += 1
            else:
                if not stack:
                    return False
                v1 = stack.pop()
                if openList.index(v1) == closeList.index(s[i]):
                    i += 1
                else:
                    return False



        if stack:
            return False
        else:
            return True
            

