from typing import List
from recursion.basic_recursion import reverse_array


def set_zeros(nums:List[List[int]]) -> None:
    n = len(nums)
    m = len(nums[0])

    rows = [False] * n
    cols = [False] * m

    for row in range(n):
        for col in range(m):
            if nums[row][col] == 0:
                rows[row] = True
                cols[col] = True

    for row in range(n):
        for col in range(m):
            if rows[row] or cols[col]:
                nums[row][col] = 0


def rotate_by_ninty(matrix:List[List[int]]) -> None: 
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        reverse_array(matrix[i], 0, len(matrix[i]) - 1)


def spiral_order(matrix:List[List[int]]) -> List[int]:
    spiral: List[int] = []
    top = 0
    left = 0
    right = len(matrix[0]) - 1
    bottom = len(matrix)

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            spiral.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            spiral.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral.append(matrix[i][left])
            left += 1

    return spiral

def pascals_triangle(numRows:int) -> List[List[int]]:
    ans:List[List[int]] = []

    for i in range(numRows):
        ans.append([1] * (i + 1))

    for i in range(2, numRows):
        for j in range(1, len(ans[i]) - 1):
            ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]

    return ans
