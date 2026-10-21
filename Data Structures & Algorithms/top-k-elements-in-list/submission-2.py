class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen= {}
        result =[]
        freq= [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i],0) +1
        for num, count in seen.items():
            freq[count].append(num)
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result
    
        
        

        