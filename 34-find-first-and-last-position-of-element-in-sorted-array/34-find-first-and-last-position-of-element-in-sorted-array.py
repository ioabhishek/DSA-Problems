class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
        
        if len(arr) == 0:
            return ([-1, -1])
        else:
            return ([arr[0], arr[-1]])
        