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
