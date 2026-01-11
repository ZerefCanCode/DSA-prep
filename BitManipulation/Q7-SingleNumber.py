'''Given an array of integers. 
All numbers occur twice except one 
number which occurs once. Find the number.

Example :

Input:  n=7, arr[] = {2, 3, 5, 4, 5, 3, 4}
Output: 2
'''
#print(2 ^ 3)
#print(1 ^ 5)
#print(5^5^6^6^4^4^2)
# 2^2 --> 001 ^ 001 --> 000

'''The best solution is to use XOR. XOR of all array elements gives us the number with a single occurrence. The idea is based on the following two facts.

The XOR of a number with itself is 0.
XOR of a number with 0 is the number itself.
'''
def singleNumber(a):
    res = a[0]
    for num in a[1:]:
        res ^= num
    return res
arr = [2, 3, 5, 4, 5, 3, 4]
print(singleNumber(arr))