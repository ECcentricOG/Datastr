from typing import List


def largest_element(nums:List[int])-> int:
    if len(nums) < 1:
        return -1
    max = nums[0]
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
    return max


def second_largest(nums: List[int]) -> int:
    n = len(nums)

    if n < 2:
        return -1

    m = max(nums[0], nums[1])
    s = min(nums[0], nums[1])
    
    for num in nums:
        if num > m:
            s = m
            m = num
            continue

        if m > num > s:
            s = num

    return s if s != m else -1


def leaders(nums:List[int]) -> List[int]:
    n = len(nums)
    ans:List[int] = [1] * n
    count = 0
    max = float('-inf')

    for i in range(n - 1, -1, -1):
        if nums[i] > max:
            ans[0] = nums[i]
            max = nums[i]
            count += 1

    return ans[:count + 1]
