#https://leetcode.com/problems/reverse-words-in-a-string/description/
def reverseWords(self, s: str) -> str:
        word=''
        word_output_string=''
        for i in range(0,len(s)):
            #print(s[i])
            if(s[i]==' ' and word!=''):
                word_output_string=word+' '+word_output_string
                word=''
            if(s[i]!=' '):
                word=word+s[i]
        if(word!=''):
            word_output_string=word+' '+word_output_string

        #print('word_arr:',word_arr)
        return word_output_string[0:len(word_output_string)-1]


def reverseWords2(self, s: str) -> str:
    a=[]
    for i in s.split(' '):
        if i=='':
            continue
        else:
            a.append(i)
    return ' '.join(a[::-1])

s = "the sky is blue"
reverseWords(s)