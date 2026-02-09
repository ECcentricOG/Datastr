from typing import List
from warnings import warn


def print_one_to_n(n:int):
    if n <= 0:
        return
    print_one_to_n(n - 1)
    print(n)

def print_n_to_one(n:int):
    if n <= 0:
        return
    print(n)    
    print_n_to_one(n - 1)

def sum_of_n(n:int) -> int:
    if n <= 0:
        return 0
    return n + sum_of_n(n - 1)

def factorial(n:int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)
    
def revese_array(nums:List, n:int): #change the logic wrronpg this time
    pass
    if n <= len(nums) // 2:
        return

    nums[len(nums) - n], nums[n] = nums[n], nums[len(nums) - n]
    revese_array(nums, n - 1)
