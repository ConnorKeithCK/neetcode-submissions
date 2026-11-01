class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # doesn't say in place, so most intuitive approach is just to square each value then return the sorted array
        squared = [num **2 for num in nums ]

        return sorted(squared)