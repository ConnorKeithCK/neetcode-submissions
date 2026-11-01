class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1chars = {}
        s2chars = {}

        for char in s:
            s1chars[char] = 1 + s1chars.get(char, 1)

        for char in t:
            s2chars[char] = 1 + s2chars.get(char, 1)

        return s1chars == s2chars