class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result =[]
        nums =sorted(nums)
        seen = set()
        for i in range(len(nums)):
            left = i+1
            right= len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0 and ((nums[i], nums[left], nums[right])) not in seen:
                    result.append([nums[i], nums[left], nums[right]])
                    seen.add((nums[i], nums[left], nums[right]))

                    right -=1
                    left +=1

                elif nums[i] + nums[left] + nums[right] > 0:
                    right -=1
                else:
                    left +=1
        return result
                
        