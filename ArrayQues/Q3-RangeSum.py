'''Given an array arr of integers of size n. We need to compute the sum of 
elements from index i to index j. The queries consisting of 
i and j index values will be executed multiple times.'''

'''Input : n=5, arr[] = {1, 2, 3, 4, 5}
q : how many times you want to calculate the sum
i = 1, j = 3
i = 2, j = 4

Output:
9
12
'''
def rangeSumO(n,arr):
    prefix=[0]*(n+1)

    for i in range(1,n+1):
        prefix[i]=prefix[i-1]+arr[i-1]

    print(prefix)

    '''q=int(input('Enter the value of q'))
    for i in range(0,q):
        i=int(input('Enter the start index'))
        j=int(input('Enter the end index(inclusive)'))
        sum=0
        for j in range(i,j+1): #1,2,3
            sum+=arr[j]
        print('the sum for : ',j+1,' iteration is ',sum)'''


def rangeSumB(size,arr):
    q=int(input('Enter the value of q'))
    for i in range(0,q):
        i=int(input('Enter the start index'))
        j=int(input('Enter the end index(inclusive)'))
        sum=0
        for j in range(i,j+1): #1,2,3
            sum+=arr[j]
        print('the sum for : ',j+1,' iteration is ',sum)


size=int(input('Enter the array size'))
arr=[]
for i in range(0,size):
    arr.append(int(input('Enter the array elements')))

print('Here is the arr: ',arr)
rangeSumO(size,arr)