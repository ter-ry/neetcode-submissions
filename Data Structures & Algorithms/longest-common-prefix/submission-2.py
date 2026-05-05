class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            char = strs[0][i]

            for words in strs:
                if i >= len(words) or words[i] != char:
                    return result
            
            result += char
            
        return result