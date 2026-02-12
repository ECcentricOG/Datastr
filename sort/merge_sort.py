from typing import List

def merge(nums:List[int], start:int, mid:int, end:int):
    temp: List = []
    left, right = start, mid + 1

    while left <= mid and right <= end:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= end:
        temp.append(nums[right])
        right += 1

    for i in range(start, end + 1):
        nums[i] = temp[i - start]

def merge_sort(nums:List[int], start:int, end:int):
    if start >= end:
        return
    
    mid:int = (start + end) // 2
    merge_sort(nums, start, mid)
    merge_sort(nums, mid + 1, end)
    merge(nums, start, mid, end)
