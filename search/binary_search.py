from typing import List


def search(nums:List[int], target:int) -> int:
    if not nums:
        return -1

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1


def search_insert(nums:List[int], target:int) -> int:
    n = len(nums)
    start = 0
    end = n - 1

    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return target
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start
