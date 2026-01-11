def swap(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp

def partition(arr, low, high, pivot):
    i = low
    j = low
    while i <= high:
        if arr[i] > pivot:
            i += 1
        else:
            swap(arr, i, j)
            i += 1
            j += 1
    return j - 1

def quickSort(arr, low, high):
    if low < high:
        pivot = arr[high]
        pos = partition(arr, low, high, pivot)

        quickSort(arr, low, pos - 1)
        quickSort(arr, pos + 1, high)

if __name__ == "__main__":
    arr=[20,10,50,90,40,80]
    quickSort(arr, 0, len(arr) - 1)
    print("The sorted array is:", arr)
    