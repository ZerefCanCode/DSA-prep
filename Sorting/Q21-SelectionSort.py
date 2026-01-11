def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the first element is the minimum
        min_index = i
        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([20,10,50,90,40,80]))