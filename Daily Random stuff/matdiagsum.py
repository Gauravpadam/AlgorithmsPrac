class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        #Logic: Child's play

        '''
            # Whole point is summing up diagonals, use a for loop to do so
            # It's basic math, mat[i][i] , [0][0],[1][1]... are primary diag elements
            # similarly mat[i][len(mat)-1+i] represents all secondary diag elements
            * Explain this please?
                Alright, len(mat) - 1 for the array index
                subtract i from it, you get the secondary diag element, TRY IT!
            # Only catch left now, is for the odd len matrices , 3x3, 5x5 ,7x7 ...
            # They all have one repeating element, i.e. central element which is summed twice
            # How do we find it?
                * Try this
                    mat[math.floor(len(mat)/2)][math.floor(len(mat)/2)] the floor val sets the base of / 2, its okay if you use // 2 too btw
                    Make the matrix on a sheet of paper and apply this, You'll get the concept
            # Subtract this val once if odd, then return sum
            # Else return sum
            # That's it :/
        '''
        sum = 0
        for i in range(len(mat)):
            sum = sum+mat[i][i] + mat[i][len(mat)-1-i]

        if (len(mat)%2>0):
            return sum - mat[math.floor(len(mat)/2)][math.floor(len(mat)/2)]
        return sum
