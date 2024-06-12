# You are given an integer A, print A to 1 using using recursion.

# Note :- After printing all the numbers from A to 1, print a new line.

class Solution:
    # @param A : integer
    def printAto1(self, A):
        if A == 0:
            return 
        else :
            print(A , end =' ')
            self.printAto1(A-1)
    def solve(self,A):
         self.printAto1(A)
         print()