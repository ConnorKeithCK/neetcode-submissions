class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = {}
        for num in nums:
            ans[num] = 1 + ans.get(num, 0)

        return max(ans, key=ans.get)