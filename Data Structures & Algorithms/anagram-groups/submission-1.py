class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            letters= "".join(sorted(word))

            if letters not in words:
                words[letters] = []

            words[letters].append(word)  
        return list(words.values())
        


        

                
            