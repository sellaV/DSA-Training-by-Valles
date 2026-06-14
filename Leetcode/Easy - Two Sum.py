class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(len(nums)):
            num = nums[index]
            find = target - num
            if find in seen:
                return [seen[find], index]
            seen[num] = index
