from typing import List


def linear_search(nums:List[int], target:int) -> int:
    for num in nums:
        if num == target:
            return num
    
    return -1
