# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 0-indexed.).



# Problem Constraints
# 1 <= A <= 105

# 0 <= B <= min(2A - 1 - 1 , 1018)


# Example Input
# Input 1:

#  A = 3
#  B = 0
# Input 2:

#  A = 4
#  B = 4


# Example Output
# Output 1:

#  0
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Row 1: 0
#  Row 2: 01
#  Row 3: 0110
# Explanation 2:

#  Row 1: 0
#  Row 2: 01
#  Row 3: 0110
#  Row 4: 01101001


# When
# A = 1 -> 0
# A = 2 ->01
# A = 3 ->0110

# As we can see that there are two part in string (when A>=2)
# first part is repeating of (A-1)th> step and second part is also compliment of (A-1)th step

# for A = 3 -> first part - 01 ( it is same as when A == 2) second part- 10 ( compliment of when A == 2)

# We know that on every expansion, the length of String is 2(A-1)

# so what we can do when B value is <= mid we can search the result in first part of (A-1)th step solve(A-1, B)

# and when B > mid we can search the result in (A-1)th step but compliment of that index to get the actual index in 1st part we have to do B - mid.

import sys 
sys.setrecursionlimit(10**6)
def find(n,k):
        if k==0:
            return 0
        val = find(n-1,k//2)
        if k%2 == 0:
            return val
        return 1-val
class Solution:
    def solve(A,B):
        return find(A,B)