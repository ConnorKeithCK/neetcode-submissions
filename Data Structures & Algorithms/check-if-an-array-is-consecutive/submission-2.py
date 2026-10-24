class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        nums.sort()
        last = nums[0] + len(nums) - 1
        for i in range(1, len(nums), 1):
            if nums[i] != nums[i - 1] + 1:
                return False


        return True
        