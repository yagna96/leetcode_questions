# Problem Description
# Write a recursive function that checks whether string A is a palindrome or Not.
# Return 1 if the string A is a palindrome, else return 0.

# Note: A palindrome is a string that's the same when read forward and backward.



# Problem Constraints
# 1 <= |A| <= 50000

# String A consists only of lowercase letters.



# maximum recursion depth in python is 1000 , we need to reset it 
import sys 
sys.setrecursionlimit(10**6)

class Solution:

    # @param A : string
    # @return an integer
    def solve(self, A):
        return self.check(A,0,len(A)-1)
    def check(self, A,i,j):
        if i>=j:
            return 1
        if A[i]==A[j]:
            return self.check(A,i+1,j-1) 
        return 0