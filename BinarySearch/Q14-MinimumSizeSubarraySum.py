#https://leetcode.com/problems/minimum-size-subarray-sum/

# Function to check if any window of size k works
def can_find(prefix,n,k):
    for i in range(n - k + 1):
        window_sum = prefix[i + k] - prefix[i]
        if window_sum >= target:
            return True
    return False

def minSubArrayLen(target, nums):
        n = len(nums)

        # Step 1: Prefix Sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        print(prefix)


        # Step 3: Binary Search on window size
        left, right = 1, n
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can_find(prefix,n,mid):
                ans = mid       # mid is a valid window size
                right = mid - 1  # try smaller
            else:
                left = mid + 1   # try larger

        return ans

target = 7
nums = [2,3,1,2,4,3]
minSubArrayLen(target,nums)
