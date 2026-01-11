'''Given an array of N positive integers. The task is to find the maximum value of 
|arr[i] – arr[j]| + |i – j|, 
where 0 <= i, j <= N – 1 and arr[i], arr[j] belong to the array.'''
import sys

def findMaxB(arr):
    maxValue=0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if (abs(arr[i]-arr[j])+abs(i-j)> maxValue):
                maxValue=abs(arr[i]-arr[j])+abs(i-j)
    return maxValue

def findMaxO(arr):
    #|arr[i] – arr[j]| + |i – j| --> arr[i] - arr[j] + i - j --> arr[i] + i - [arr[j]+ j]
    # arr[i] -arr[j] - i + j --> arr[i] - i - (arr[j] - j)
    # - arr[i] +arr[j] + i - j ---> arr[j]-j - (arr[i]- i)
    # -arr[i] +arr[j] -i +j --> arr[j]+j - (arr[i]+j)
    max1= -sys.maxsize #arr[i]+i
    max2= -sys.maxsize #arr[i]-i
    min1= sys.maxsize #arr[i]+i
    min2= sys.maxsize #arr[i]-i
    for i in range(0,len(arr)):
        temp1=arr[i]+i
        temp2=arr[i]-i
        max1=max(temp1,max1)
        max2=max(temp2,max2)
        min1=min(temp1,min1)
        min2=min(temp2,min2)

    return max(max1-min1 , max2-min2)
    

size=int(input('Enter the size of array'))
arr=[]
for i in range(0,size):
    arr.append(int(input('Enter the element')))

print('Array is: ',arr)
maxValue=findMaxO(arr)
print('maxValue of |arr[i] – arr[j]| + |i – j| is ',maxValue)