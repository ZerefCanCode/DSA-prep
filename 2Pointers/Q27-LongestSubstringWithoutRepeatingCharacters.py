class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        j=0
        i=0

        max_len=0
        map={}

        while(j<len(s)):
            #print(map)
            if(s[j] not in map.keys()):
                map[s[j]]=1 #aquire
            else:
                #start releasing
                while(s[i]!=s[j]):
                    map[s[i]]-=1
                    #print('here')
                    #print(map)
                    if(map[s[i]]==0):
                        #print('here2')
                        map.pop(s[i])
                    i+=1
                i+=1
            if(len(map)>max_len):
                max_len=len(map)
            j+=1

        return max_len
                

        