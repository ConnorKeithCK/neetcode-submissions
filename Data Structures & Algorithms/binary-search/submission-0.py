class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 # beginning of the array
        right = len(nums) - 1 # index of the last element of the array

        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                # Target sits to the LEFT of the midpoint, therefore the RIGHT pointer needs to move
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                # Target == mid
                return mid
        
        return -1