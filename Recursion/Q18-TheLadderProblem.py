#ques- You are standing at the bottom of a ladder with N steps.
'''You can climb either:

1 step at a time

2 steps at a time

3 steps at a time
(… in general, k steps depending on the version)

Question:
How many distinct ways can you reach the top?'''

def ways_to_climb(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    return (ways_to_climb(n-1) +
            ways_to_climb(n-2) +
            ways_to_climb(n-3))

# Example
print(ways_to_climb(4))  # Output: 7
