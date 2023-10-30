from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = {}
        for i in range(0, len(nums)):
            remainder = target - nums[i]
            if remainder in obj:
                return [i, obj[remainder]]
            obj[nums[i]] = i
