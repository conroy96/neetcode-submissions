class Solution:
    #max(l,r) *len(heights[l:r:])
    def maxArea(self, heights: List[int]) -> int:
        l= 0
        r = len(heights)-1
        ans = min(heights[l],heights[r]) * len(heights[l:r:1])
        while l < r:
            current = min(heights[l],heights[r]) * len(heights[l:r:1])
            if heights[l] >= heights[r] and ans < current:
                ans = current
                r -=1

            elif heights[l] <= heights[r] and ans < current:
                ans = current
                l+=1

            elif heights[l] <= heights[r] and ans == current:
                l+=1

            elif heights[l] >= heights[r] and ans == current:
                r-=1
            if heights[l] >= heights[r] and ans > current:
                
                r -=1

            elif heights[l] <= heights[r] and ans > current:
                
                l+=1
            
        return ans

             
        