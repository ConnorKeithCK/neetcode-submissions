class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        window = set()

        for r in range(len(nums)):
            if r - left > k:
                window.remove(nums[left])
                left += 1
            if nums[r] in window:
                return True

            window.add(nums[r])

        return False
