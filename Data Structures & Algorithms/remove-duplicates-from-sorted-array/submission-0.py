class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dups = 0

        left = 0
        right = 1

        while left < right and right < len(nums):
            print(nums[left], ":", nums[right])
            if nums[left] == nums[right]:
                nums.pop(right)
                continue
            left += 1
            right += 1

        return len(nums)