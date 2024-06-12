# Given a number A, we need to find the sum of its digits using recursion.


# Problem Constraints
# 1 <= A <= 109

class Solution:
    # @param A : integer
    # @return an integer

    def solve(self, A):
        if A == 0:
           return  0
        else :
            return A%10 + self.solve(A//10)