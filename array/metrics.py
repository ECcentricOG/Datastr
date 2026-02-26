from typing import List


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
