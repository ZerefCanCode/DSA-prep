'''Find the position of the first 1 
from right to left, in the binary 
representation of an Integer.

Examples:

Input: n = 18
Output: 2
'''

def leastSignificantBit(n):
    if n == 0:
        return 0
    else:
        pos = 1
        for i in range(32):
            if (n & (1 << i)) == 0:
                pos += 1
            else:
                break
        return pos
    
print(leastSignificantBit(18))