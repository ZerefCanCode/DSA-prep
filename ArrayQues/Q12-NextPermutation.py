#https://leetcode.com/problems/next-permutation/


def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    drop_idx=-1

    for i in range(len(nums)-1,0,-1):
        #print(nums[i])
        if(nums[i-1]<nums[i]): #drop detected
            drop_idx=i-1
            break 
    #print(drop_idx)
    if(drop_idx==-1):
        nums.reverse()
        return
    #find idx of next highest element
    next_largest=-1
    for i in range(len(nums)-1,drop_idx,-1):
        if(nums[drop_idx]<nums[i]):
            next_largest=i
            break
            

    
    nums[drop_idx],nums[next_largest]=nums[next_largest],nums[drop_idx]
    #print(nums)

    nums[drop_idx+1:]=reversed(nums[drop_idx+1:])

        
        


        

        
        