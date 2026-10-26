class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort so the shortest string is the one iterated over
        strs.sort()
        i = 0
        while i < len(strs[0]) and strs[0][i] == strs[-1][i]:
            i += 1

        return strs[0][:i]