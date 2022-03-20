class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        lst = []
        for i in range(len(nums)):
            remaining = target-nums[i]

            if remaining in seen:
                lst.append(seen[remaining])
                lst.append(i)
                break
            else:
                seen[nums[i]] = i
        return lst