class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_a={}
        freq_b={}
        for i in range(len(s)):
            if s[i] not in freq_a:
                freq_a[s[i]] =1
            else:
                freq_a[s[i]] +=1

            if t[i] not in freq_b:
                freq_b[t[i]] =1
            else:
                freq_b[t[i]] +=1
        return freq_a == freq_b
            
            
            

        