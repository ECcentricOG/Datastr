from recursion.basic_recursion import reverse_array

arr = [1,2,3,4,5]
arr1 = [1,2,3,4]

#reverse_array(arr, 0, len(arr) - 1)
#reverse_array(arr1, 0, len(arr1) - 1)
reverse_array(arr, 2, len(arr) - 1)
reverse_array(arr1, 1, len(arr1) - 1)

print(arr)
print(arr1)
