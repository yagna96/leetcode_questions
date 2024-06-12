# Problem Description
# You are given an integer A, print 1 to A using using recursion.

# Note :- After printing all the numbers from 1 to A, print a new line.



# Problem Constraints
# 1 <= A <= 104

import sys
sys.setrecursionlimit(10**6)
def print1toA(A):
    if(A == 0):
        return
    print1toA(A - 1)
    # end the print with space 
    print(A , end=' ')
class Solution:
    # @param A : integer
    def solve(self, A):
        print1toA(A)
        # prints new line 
        print()  