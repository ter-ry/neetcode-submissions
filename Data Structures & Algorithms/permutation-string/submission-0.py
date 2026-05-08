class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for i in range(len(s1)):
            freq[s1[i]] = freq.get(s1[i], 0) + 1

        window = {}
        left = 0

        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1
            while right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            
            
            if window == freq:
                return True
        
        return False

        