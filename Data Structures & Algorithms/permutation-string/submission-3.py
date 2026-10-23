class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d = {}
        s2_d = {}
        for i in range(len(s1)):
            s1_d[s1[i]] = s1_d.get(s1[i],0) +1
        
        left =0
        for right in range(len(s2)):
            while right - left + 1 > len(s1):
                s2_d[s2[left]] -=1
                if s2_d[s2[left]] ==0:
                    del s2_d[s2[left]]
                left +=1
            s2_d[s2[right]]= s2_d.get(s2[right],0) +1
            if s1_d == s2_d:
                return True
        return False
        