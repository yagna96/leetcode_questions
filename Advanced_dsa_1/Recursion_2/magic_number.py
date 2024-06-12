# Problem Description
# Given a number A, check if it is a magic number or not.

# A number is said to be a magic number if the sum of its digits is calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1, then the number is a magic number.



# Problem Constraints
# 1 <= A <= 109



# Input Format
# The first and only argument is an integer A.



# Output Format
# Return an 1 if the given number is magic else return 0.

import sys 
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : integer
    # @return an integer
    def sum_of_digits(self,A):
        if A <10:
            return A
        sum_=0
        while A>0:
             sum_=sum_+ A%10 
             A=A//10
        return self.sum_of_digits(sum_)
    
    def solve(self, A):
        if self.sum_of_digits(A)==1:
            return 1
        return 0