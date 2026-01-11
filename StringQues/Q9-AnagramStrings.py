#https://leetcode.com/problems/valid-anagram/description/
def isAnagram(self, s: str, t: str) -> bool:
    dict1={}
    if(len(s)!=len(t)):
        return False
    for letter in s:
        if(letter not in dict1.keys()):
            dict1[letter]=s.count(letter)
    #print('dict1: ',dict1)
    for letter in t:
        #print(letter)
        if(letter not in dict1.keys()):
            return False 
        else:
            dict1[letter]=dict1.get(letter)-1
            if(dict1.get(letter)==0):
                #print('popping letter:',letter)
                dict1.pop(letter)
            
    #print('dict1: ',dict1)
    if(len(dict1)==0):
        return True 
    return False

    '''if(len(s)!=len(t)):
            return False
        if(Counter(t)==Counter(s)):
            return True
        return False'''
    
isAnagram("anagram","nagaram")
        