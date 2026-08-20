class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        count = 0
        result = []
        for n in range(len(nums),0,-1):    
            for key,value in counter.items():
                if value==n:
                    result.append(key)
                    count+=1
                if count==k:
                    return result
                
        
                    

        