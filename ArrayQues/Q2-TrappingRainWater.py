'''Given n non-negative integers representing 
an elevation map where the width of 
each bar is 1, compute how much water it can trap after rain.'''

#calculating left max and right max for each element
# min(leftmax,rightmax)-currentElement
import sys
def TrappingRainWaterB(n, arr):
    storage=0
    for i in range(1,n-1):
        #left max
        left_max=-sys.maxsize
        for j in range(0,i):
            if(left_max<arr[j]):
                left_max=arr[j]

        #right max
        right_max=-sys.maxsize
        for j in range(i+1,n):
            if(right_max<arr[j]):
                right_max=arr[j]
        print('for element: ',arr[i],' left max: ',left_max,' right max: ',right_max)
        if(min(left_max,right_max)-arr[i]>0):
            storage+=(min(left_max,right_max)-arr[i])
    return storage

def TrappingRainWaterO(n, arr):
    storage=0
    leftMax=[0]
    rightMax=[0]
    for i in range(1,n):
        #left max
        left_max=max(arr[i-1],leftMax[-1])
        leftMax.append(left_max)
    for i in range(n-2,-1,-1):
        #right max
        right_max=max(arr[i+1],rightMax[-1])
        rightMax.append(right_max)
    
    rightMax.reverse()
    print(leftMax)
    print(rightMax)
    for i in range(0,n):
        print(min(leftMax[i],rightMax[i])-arr[i])
        if((min(leftMax[i],rightMax[i])-arr[i])>0):
            storage+=(min(leftMax[i],right_max[i])-arr[i])
            print('storage: ',storage)
    return storage

n=11
height= [1,0,2,1,0,1,3,2,1,2,1]
print(TrappingRainWaterO(n, height))