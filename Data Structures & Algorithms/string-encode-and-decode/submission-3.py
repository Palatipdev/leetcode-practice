class Solution:

    def encode(self, strs: List[str]) -> str:

        join = ""
        for myString in strs:
            join += str(len(myString))
            join += "#"
            join += myString
        return join
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        finalList = []
        i, j = 0, 0
        while j < len(s):
            if s[i].isdigit():
                num = ""
                while s[i].isdigit():
                    num += s[i]
                    i += 1
                    j += 1
                    if (s[i] == "#"):
                        break
                j += int(num) + 1
                i += 1
            finalList.append(s[i:j])
            i = j
        return finalList
        
     
