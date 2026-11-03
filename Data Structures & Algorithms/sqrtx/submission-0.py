class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid ** 2 < x:
                left = mid + 1
                # we need a larger base value
            elif mid ** 2 > x:
                # smaller value, decrease rightr
                right = mid - 1
            else:
                return mid

        return right