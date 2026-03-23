from typing import List


def quick_sort(nums:List[int], left:int, right:int):
    if left < right:
        privot = partition(nums, left, right)
        
        quick_sort(nums, left, privot - 1)
        quick_sort(nums, privot + 1, right)

def partition(nums:List[int], left:int, right:int) -> int:
    pivot = nums[right]
    i = left - 1

    for j in range(left, right):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[right] = nums[right], nums[i + 1]

    return i + 1
