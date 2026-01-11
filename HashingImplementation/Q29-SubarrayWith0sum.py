'''n=5 ,arr[]={4, 2, -3, 1, 6}
prefix sum --> [4,6,3,4,10]'''

if __name__ == "__main__":
    n = int(input())
    a = [int(input()) for _ in range(n)]

    sum = 0
    prefix_sums = {}

    for i in range(n):
        sum += a[i]

        # Check if the sum is zero or already seen
        if sum == 0 or sum in prefix_sums:
            print("YES")
            exit()

        # Store the prefix sum in the map
        prefix_sums[sum] = i

    print("NO")