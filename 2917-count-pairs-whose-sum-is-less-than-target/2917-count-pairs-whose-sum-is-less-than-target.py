
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0  
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if n>j>i>=0 :
                    if nums[i] + nums[j] < target:
                        count += 1
                    
                
        
        return count





                