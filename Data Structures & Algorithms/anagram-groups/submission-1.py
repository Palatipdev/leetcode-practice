class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDick = defaultdict(list)

        for word in strs:
            count = [0] * 26 # a to z
            for char in word:
                count[ord(char) - ord("a")] += 1
            myDick[tuple(count)].append(word)
        
        return list(myDick.values())