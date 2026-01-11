def two_sum_two_pointer(nums, target):
    # Store value + original index
    arr = [(nums[i], i) for i in range(len(nums))]
    
    # Sort based on value
    arr.sort()

    left = 0
    right = len(arr) - 1

    while left <= right:
        current_sum = arr[left][0] + arr[right][0]

        if current_sum == target:
            return [arr[left][1], arr[right][1]]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return []  # no solution
