class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        count = 1
        longest= 0
        if len(new_nums) == 0:
            return 0

        for i in range(len(new_nums)-1):
            if (((new_nums[i+1]) - (new_nums[i])) == 1):
                count+=1
            elif (((new_nums[i+1]) - (new_nums[i])) == 0):
                pass
            elif (((new_nums[i+1]) - (new_nums[i])) != 1):
                longest = max(count,longest)
                count =1
                continue
        longest = max(count,longest)
        return longest

            

            


                

        