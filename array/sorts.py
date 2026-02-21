from typing import List

def is_sorted_rotated(nums:List)-> bool:
    n = len(nums)
    count = 0

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
    return count <= 1

def sort_colors(nums:List[int]) -> None:
    start, end, mid = 0, 0, len(nums) - 1
    
    while mid <= end:
        if nums[mid] == 0:
            nums[start], nums[mid] = nums[mid], nums[start]
            start += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[end] = nums[end], nums[mid]
            end -= 1
        else:
            mid += 1
