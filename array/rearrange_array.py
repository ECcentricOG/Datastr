from typing import List


def rearrange_array_by_sign(nums:List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * n
    left, right = 0, 1

    for num in nums:
        if num >= 0:
            ans[left] = num
            left += 2
        else:
            ans[right] = num
            right += 2

    return ans
