from typing import List

#No with duplicates duplicated 
def union_two_sorted_array(nums1:List[int], nums2:List[int]) -> List:
    n = len(nums1)
    m = len(nums2)
    ans = []
    
    i, j = 0, 0

    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            ans.append(nums1[i])
            i += 1
        else:
            ans.append(nums2[j])
            j += 1

    while i < n: 
        ans.append(nums1[i])
        i += 1
        
    while j < m:
        ans.append(nums2[j])
        j += 1

    return ans
