class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        res = []

        shortest = word1 if len(word1) < len(word2) else word2

        while w1 < len(shortest):
            res.append(word1[w1])
            res.append(word2[w1])

            w1 += 1

        res.append(word1[w1:])
        res.append(word2[w1:])

        return "".join(res)