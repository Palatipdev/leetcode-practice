class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # plan with ai telling to use dictionary and nidge me to use sorted
        # build a dictionary that has key as the word as sorted character and value is a list of anagrams. now before adding in every new word check whether that sorted version of the word exist as a key if so add that in
        # O(n)

        myDick = {}

        
        for word in strs:
            key = str(sorted(word))
            if key in myDick:
                myDick[key].append(word)
            else:
                myDick[key] = [word]
        return list(myDick.values())
