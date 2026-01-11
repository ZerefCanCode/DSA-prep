def allPermutations(arr,flags,ans,n):
    if(all(flags)==True):
        print(ans)
        return
    
    for i in range(0,n):
        if(flags[i]==False):
            flags[i]=True
            ans.append(arr[i])
            allPermutations(arr,flags,ans,n)
            ans.pop()
            flags[i]=False
            

allPermutations([1,2,3],[False,False,False],[],3)

#[1,2,3] , [F,F,F] ,[], 3
#[1,2,3] ,[T,F,F] ,[1] ,3
#[1,2,3], [T,T,F], [1,2],3
#[1,2,3],[T,T,T],[1,2,3] ,3 
# print -- [1,2,3]
#[1,2,3] ,[T,F,T] ,[1,2] ,3