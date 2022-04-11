class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        flag = True
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
                
        for x,y in d.items():
            if y >= 2:
                flag = True
                break
            else:
                flag = False
        
        return flag
        