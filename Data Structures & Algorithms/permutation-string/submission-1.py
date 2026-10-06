class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size= len(s1)
        left = 0
        s1_dict={}
        s2_dict = {}
        for i in range(len(s1)):
            s1_dict[s1[i]] = s1_dict.get(s1[i], 0) +1

        first_window= s2[:window_size]
        for j in range(len(first_window)):
            s2_dict[first_window[j]] = s2_dict.get(first_window[j],0) + 1

        if s1_dict == s2_dict:
            return True

        for right in range(window_size,len(s2)):
                s2_dict[s2[right]] = s2_dict.get(s2[right], 0) +1
                s2_dict[s2[right - window_size]] -=1
                if s2_dict[s2[right - window_size]] ==0:
                    del s2_dict[s2[right - window_size]]
                if s1_dict ==s2_dict:
                    return True
        return False


        

        

       
    
        



        