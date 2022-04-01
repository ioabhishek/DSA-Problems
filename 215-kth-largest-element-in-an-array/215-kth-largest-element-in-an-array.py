class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
        
        #using insertion sort method
#         for i in range(1, len(nums)):
#             key = nums[i]
#             j = i-1
            
#             while j >= 0 and key < nums[j]:
#                 nums[j+1] = nums[j]
#                 j = j-1
#             nums[j+1] = key
            
#         return (nums[len(nums)-k])