class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        swaps = 0
        while left <= right:
            if nums[left] != val:
                left += 1
                continue
            if nums[right] == val:
                right -= 1
                continue   

            if nums[left] == val:
                tmp = nums[right]
                nums[right] = nums[left]
                nums[left] = tmp
            
                left += 1
                right -= 1

        return left
        

