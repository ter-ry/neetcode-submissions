class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        out = [nums for nums, freq in res[:k]]
        return out