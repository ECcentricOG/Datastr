from typing import List


def count_frequencies(nums:List[int]):
    tracker = {}

    for num in nums:
        if num in tracker:
            tracker[num] += 1
        else:
            tracker[num] = 1

    print(tracker)
