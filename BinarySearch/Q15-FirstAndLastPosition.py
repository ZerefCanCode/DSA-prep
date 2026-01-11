#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

def binarySearch(nums,target,s,e):
    while(s<=e):
        mid=(e+s)//2
        #not found
        if(nums[mid]<target):
            s=mid+1
        elif(target<nums[mid]):
            e=mid-1
        else: #if found
            while(s-1>=0 and nums[s-1]==target):
                s=s-1
            while(e+1<len(nums) and nums[e+1]==target):
                e+=1
            return s,e

def searchRange(nums, target):
    if(len(nums)==0):
        return [-1,-1]
    if(target not in nums):
        return [-1,-1]
    if(len(nums)==1 and target in nums):
        return [0,0]

    s,e=binarySearch(nums,target,0,len(nums)-1)
    #print('s:',s,'e:',e)
    min_idx=len(nums)
    max_idx=-1
    for i in range(s,e+1):
        if(nums[i]==target):
            if(min_idx>i):
                min_idx=i
            if(max_idx<i):
                max_idx=i
    
    return [min_idx,max_idx]


        
        