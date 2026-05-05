class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in seen:
                return [seen[remainder], i]
            else:
                seen[nums[i]] = i