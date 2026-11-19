class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        currCount = {}
        left = 0
        # create a map of each char in s1 and the #
        for s in s1:
            count[s] = count.get(s, 0) + 1

        for r in range(len(s2)):
            if s2[r] not in s1:
                left = r + 1
                currCount = {}
                continue

            currCount[s2[r]] = currCount.get(s2[r], 0) + 1
            
            if r - left + 1 == len(s1):
                if currCount == count:
                    return True
                else:
                    currCount[s2[left]] = currCount[s2[left]] - 1 if currCount[s2[left]] > 0 else currCount.pop(left)
                    left += 1
            
        return False