from typing import List

def sort(nums: List)-> List:
    n = len(nums)
    for i in range(n - 1, -1, -1):
        swapped = False
        for j in range(i):
            if(nums[j] > nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if(swapped == False):
            return nums
    return nums
