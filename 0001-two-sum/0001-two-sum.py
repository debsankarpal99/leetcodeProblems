class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = []
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    r = i, j
                    return r