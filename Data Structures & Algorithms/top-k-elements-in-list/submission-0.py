class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dictionary 
        freq={}
        result = []
        for i in nums:
            #If the number in the list is not in the dictionary create a key for it and set the value to 1
            if i not in freq:
                freq[i]= 1
            #if it is present as a key increment the value 
            else:
                freq[i] +=1

        sorted_items =sorted( #sort the following
        freq.items(), # function to give both key and value of dict
        key =lambda x: x[1], #the key is x and what we are extracting is the second element therefore x[1]
        reverse = True # normally sort is acending order this makes it descending
        )

        for item in sorted_items[:k]:
            result.append(item[0])
        return result



        

            
        
