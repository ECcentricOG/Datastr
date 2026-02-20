from typing import List


def longest_subarray_of_sum(nums:List[int], k:int) -> int:

    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    left, right = 0, len(nums) - 1

    while left <= right:
        rem = nums[right] - nums[left]
        if rem > k:
            right -= 1
        elif rem < k:
            left += 1
        else:
            return right - left 

    return 0
