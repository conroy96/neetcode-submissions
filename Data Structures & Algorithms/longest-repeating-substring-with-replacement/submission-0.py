class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        seen ={}
        best = 0
        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) +1

            while (right - left +1) - max(seen.values()) > k:
                seen[s[left]] -=1

                if seen[s[left]] == 0:
                    del seen[s[left]]
            
                left+=1

            best = max(best, right - left +1)
        return best
        