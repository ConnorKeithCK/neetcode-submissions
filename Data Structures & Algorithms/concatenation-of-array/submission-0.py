class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums[:]
        for num in nums:
            result.append(num)

        return result