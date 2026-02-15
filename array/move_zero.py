from typing import List

def move_zeros(nums:List[int]) -> None:
    n = len(nums)
    show = 0

    for fast in range(n):
        if nums[fast] != 0 and nums[show] == 0:
            nums[fast], nums[show] = nums[show], nums[fast]

        if nums[show] != 0:
            show += 1
