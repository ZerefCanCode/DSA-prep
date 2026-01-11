'''Kth Bit is set or not:
Given a number N and a bit number K, check if the Kth bit of N is set or not.
 A bit is called set if it is 1.
'''
def isKthBitSet(n, k):
    print('n >> k',n >> k)
    if ((n >> k) & 1) == 1:
        print("SET")
    else:
        print("NOT SET")

def isKthBitSet2(n,k):
    if n & (1 << k):
            print("SET")
    else:
        print("NOT SET")


#first login.. right shift by k bits
n=5 #101 --> 010 --> 2 
# 010 & 001 == 1
k=1
#isKthBitSet(n,k)

#second logic
#shifting 1 to left side.. k times
# 1= 001
# 010 & 101 = 000
# 100 & 111 = 100 = 4= non 0 -- true
isKthBitSet2(n,k)