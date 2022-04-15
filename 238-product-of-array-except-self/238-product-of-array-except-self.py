class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightProd = [1]*len(nums)
        leftProd = [1]*len(nums)
        bothProd = []

        for i in range(1, len(nums)):
            leftProd[i] = nums[i-1] * leftProd[i-1]

        for j in range(len(nums)-2,-1, -1):
            rightProd[j] = nums[j+1] * rightProd[j+1]

        for k in range(len(nums)):
            bothProd.append(rightProd[k] * leftProd[k])
        
        return bothProd
        