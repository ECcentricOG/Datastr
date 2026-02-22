from typing import List


def count_frequencies(nums:List[int]):
    tracker = {}

    for num in nums:
        if num in tracker:
            tracker[num] += 1
        else:
            tracker[num] = 1

    print(tracker)

def max_frequency(nums:List[int]) -> int:
    pass

def single_count(nums:List[int]) -> int:
    ans = 0

    for num in nums:
        ans ^= num

    return ans

def majority_element(nums:List[int]) -> int:
   # track = {}
   # n = len(nums)

   # for num in nums:
   #     if num in track:
   #         track[num] += 1
   #     else:
   #         track[num] = 1

   #     if track[num] > n // 2:
   #         return num

    ele = 0
    count = 0

    for num in nums:
        if count == 0:
            ele = num

        if ele == num:
            count += 1
        else:
            count -= 1

    return ele
