class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        
        n = len(nums) + 1
        
        return (floor(n*(n-1)/2)-sum)
        