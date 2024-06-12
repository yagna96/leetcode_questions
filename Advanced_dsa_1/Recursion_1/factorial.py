# Problem Description
# Write a program to find the factorial of the given number A using recursion.

# Note: The factorial of a number N is defined as the product of the numbers from 1 to N.


# Problem Constraints
# 0 <= A <= 12
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A ==1:
            return 1
        else:
            return self.solve(A-1)*A