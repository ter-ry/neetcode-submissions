class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = ''
        for i in s:
            if i.isalnum():
                test += i.lower()
        return test == test[::-1]