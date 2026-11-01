class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # could this be solved with prefix sum....?
        left = 0
        right = len(heights) - 1

        maxArea = 0
        
        while left < right:
            maxArea = max(maxArea, (right - left) * min(heights[left], heights[right]))
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxArea
