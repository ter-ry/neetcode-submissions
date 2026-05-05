class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        current = nums[0]

        for i in nums[1:]:
            current = max(i, current + i)
            total = max(current, total)

        return total