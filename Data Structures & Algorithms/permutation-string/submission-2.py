class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0 
        right =0
        s1_dict = {}
        s2_dict ={}
        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1


        while right < len(s2):
            while right - left +1 > len(s1):
                s2_dict[s2[left]] -=1
                if s2_dict[s2[left]] == 0:
                    del s2_dict[s2[left]]
                left +=1
            s2_dict[s2[right]] = s2_dict.get(s2[right], 0) +1
            right +=1
            if s1_dict == s2_dict:
                return True 
        return False
