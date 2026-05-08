class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = (right - left) / 2

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                left = mid
            else:
                right = mid
            mid = (right - left) / 2
            
        return -1
