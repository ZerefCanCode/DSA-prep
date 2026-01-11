#https://leetcode.com/problems/count-pairs-of-similar-strings/description/
def similarPairs(self, words: List[str]) -> int:
    count=0
    for i in range(0,len(words)-1):
        dict_i={}
        for character in words[i]:
            if(character not in dict_i):
                dict_i[character]=1
        #print(dict_i)
        for j in range(i+1,len(words)):
            #print(words[j])
            dict_j={}
            for character in words[j]:
                if(character not in dict_j.keys()):
                    dict_j[character]=1
            if(dict_i==dict_j):
                count+=1
    return count

similarPairs(["aba","aabb","abcd","bac","aabc"])


        