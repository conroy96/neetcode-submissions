class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        current =0
        best = 0
        if len(s)== 0:
            return 0
        elif len(s) == 1:
            return 1
        for right in range(len(s)):
            while s[right] in seen:
                current = len(seen)
                if current > best:
                    best =current

                seen.remove(s[left])
                left+=1

            seen.add(s[right])
        if len(seen) > best:
            best = len(seen)
        return best
  