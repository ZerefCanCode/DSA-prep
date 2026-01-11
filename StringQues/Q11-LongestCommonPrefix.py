#https://leetcode.com/problems/longest-common-prefix/description/


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    match=0

    for vals in zip(*strs):
        print(vals)
        if len(set(vals))==1:
            match+=1
        else:
            break
    if(match == 0):
        return ""
    
    return strs[0][:match]

strs=["flower","flow","flight"]
print(longestCommonPrefix(strs))