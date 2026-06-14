# First Solution - Create a dictionanry before checking the elements - Time complexity: O(2n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_find = {}
        for index in range(len(nums)):
            map_find[nums[index]] = index
        for i in range(len(nums)):
            find = target - nums[i]
            if find in map_find and i != map_find[find]:
                return [i, map_find[find]]

# Second Solution - After comparing to solution -> Optimize with One-pass hash map - Time complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_find = {}
        for index in range(len(nums)):
            find = target - nums[index]
            if find in map_find:
                return [map_find[find], index]
            map_find[nums[index]] = index
