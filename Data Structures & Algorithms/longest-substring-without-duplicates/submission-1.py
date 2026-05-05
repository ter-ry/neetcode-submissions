class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = best = 0
        seen = set()

        for right in range(len(s)):
            char = s[right]
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            best = max(best, right - left + 1)
        
        return best
