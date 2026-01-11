#https://leetcode.com/problems/merge-intervals/description/
#given a list of intervals--[start,end]
#output: an array of non-overlapping intervals
#problem : merge overlapping intervals --> criteria for non-overlapping interval--
'''if start of 2nd interval is after the end of first interval
criteria or vice versa. Now overlapping can be of three types : either interval 2 is 
completely inside interval 1 or vice verse, start of second is before or 
equals end of first, start of first is before end of second'''



def merge(intervals: List[List[int]]):
    #base condition
    if(len(intervals)<2):
        return intervals

    intervals_sorted=sorted(intervals)
    print(intervals_sorted)
    idx=0
    while(True):
        overlap_flag=False
        if(idx+1<len(intervals_sorted) and intervals_sorted[idx][1]<intervals_sorted[idx+1][0]):
            overlap_flag=False
            idx+=1
        else:
            overlap_flag=True
            if(idx+1<len(intervals_sorted)):
                #print(True)
                combined_interval=[intervals_sorted[idx][0],max(intervals_sorted[idx][1],intervals_sorted[idx+1][1])]
                intervals_sorted.pop(idx)
                intervals_sorted.pop(idx)
                intervals_sorted.insert(idx,combined_interval)
        if(idx>=len(intervals_sorted)-1):
            break
    
    #print(intervals)
    return intervals_sorted


        