class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        numCount = {}
        for i in range(len(nums)):
            if nums[i] in numCount:
                numCount[nums[i]] += 1
            else:
                numCount[nums[i]] = 1
                
        maxx = max(numCount.values())
        keys = [k for k, v in numCount.items() if v == maxx]
        return (keys[0])
