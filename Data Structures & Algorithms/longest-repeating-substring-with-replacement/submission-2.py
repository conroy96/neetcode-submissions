class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        
        counts ={}
        result =0
        while right < len(s):
            counts[s[right]] = counts.get(s[right],0)+1

            while (right - left +1) - max(counts.values()) > k:
                counts[s[left]] -=1 

                left +=1
            current = right - left +1
            result  = max(current, result)
            right +=1
        return result



