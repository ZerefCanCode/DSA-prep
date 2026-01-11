def merge_sort(arr):
    if len(arr) <= 1:
        return arr
   
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
   
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
   
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0
   
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
   
    result.extend(left[i:])
    result.extend(right[j:])
   
    return result

print(merge_sort([20,10,50,90,40,80]))

