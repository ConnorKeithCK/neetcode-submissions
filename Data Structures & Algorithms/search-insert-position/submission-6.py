class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        lastValue = 0

        while left <= right:
            mid = (left + right) // 2
            lastValue = mid
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid

        # We know this is sorted
        # If value is not found, we simply check if the target is < or > the LAST value checked, because we know it will have to sit either before or after it as a result of it being a sorted array.
        return left