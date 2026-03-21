from typing import List

def move_zeros(nums:List[int]) -> None:
    n = len(nums)
    slow = 0

    for fast in range(n):
        if nums[slow] == 0 and nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        if nums[slow] != 0:
            slow += 1
