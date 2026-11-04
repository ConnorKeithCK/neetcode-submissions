class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        # let's iterate from the end of it!'
        for i in range(len(matrix) - 1, -1, -1):
            # is the first value in the this matrix LARGER than the target? If so, skip it and go to the next!
            if matrix[i][0] > target:
                continue
            # We have the matrix where the first value in the matrix is LESS than the target, and we know the first value of the next matrix is LARGER than the target. Therefore, it either exists in this matrix or not at all!
            if matrix[i][-1] < target:
                return False
                # Largest value in this matrix is larger than targer, return false.

            left = 0
            right = len(matrix[i]) - 1

            while left <= right:
                mid = (left + right) // 2

                if matrix[i][mid] > target:
                    right = mid - 1
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    return True

        return False
