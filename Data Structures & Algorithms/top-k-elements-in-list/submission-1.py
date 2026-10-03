class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= defaultdict(int)
        result=[]
        

        for i in nums:
            freq[i] +=1
        ordered= sorted(freq.items(),key=lambda item : item[1], reverse = True)
        for j in ordered:


            if len(result) == k:
                return result
            else:
                result.append(j[0])
        return result


            
            
        