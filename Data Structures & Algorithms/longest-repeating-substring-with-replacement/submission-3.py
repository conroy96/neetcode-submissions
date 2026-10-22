class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left= 0
        right =0 
        best = 0
        seen ={}
        while right < len(s):
            seen[s[right]] = seen.get(s[right],0)+1

            while (right - left +1) - max(seen.values()) > k:
                seen[s[left]] -=1
                if seen[s[left]] ==0:
                    del seen[s[left]]
                left +=1

            current = right - left +1
            best=  max(best , current)
            right +=1
        return best

        