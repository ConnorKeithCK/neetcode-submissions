class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1 # With the LARGEST and SMALLEST number, the value is larger than target. Therefore, we know the RIGHT number can NOT be correct, but the smallest might. Decrease right counter
            if numbers[left] + numbers[right] < target:
                left += 1

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

        return [left + 1, right + 1]