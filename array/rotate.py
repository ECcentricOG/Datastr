from typing import List

def left_rotate(nums:List[int], k:int) -> None:
    n = len(nums) 
    k = k % n

    for _ in range(k):
        temp = nums[0]
        for j in range(1, n):
            nums[j - 1] = nums[j]

        nums[-1] = temp

def rotate(nums:List[int], k:int) -> None:
    n = len(nums)
    k = k % n

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)


def reverse(nums:List[int], start:int, end:int) -> None:
    if start >= end:
        return

    nums[start], nums[end] = nums[end], nums[start]

    reverse(nums, start + 1, end - 1)
