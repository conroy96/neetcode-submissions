class Solution:
    def trap(self, height: List[int]) -> int:
        left =0
        right = len(height)-1
        left_best , right_best = height[left] , height[right]
        total =0

        while left < right:
            if left_best < right_best:
                left+=1
                left_best = max(left_best,height[left])
                total += left_best - height[left]
            else:
                right-=1
                right_best = max(right_best , height[right])
                total += right_best - height[right]
        return total