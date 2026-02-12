from sort.merge_sort import merge_sort


test_arr = [42, -7, 1024, 0, 56, -7, 88, 12, 999, 3, 15, 22]

merge_sort(test_arr, 0, len(test_arr) - 1)

print(test_arr)
