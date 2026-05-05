class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def anagram(x):
            count = {}
            for i in x:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
            return count

        return anagram(s) == anagram(t)