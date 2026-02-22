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


# Kadane's algorithm
def max_sum_subarray(nums:List[int]) -> int:
    max = float('-inf')
    sum = 0

    for num in nums:
        sum += num

        if sum > max:
            max = sum

        if sum < 0:
            sum = 0

    return int(max)
