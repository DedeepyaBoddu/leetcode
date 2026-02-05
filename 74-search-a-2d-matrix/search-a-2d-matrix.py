class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        l = 0
        r = m*n-1

        while l<=r:
            m = (l+r)//2
            if target == matrix[m//n][m%n]:
                return True
            elif target < matrix[m//n][m%n]:
                r = m-1
            else:
                l = m+1      
        return False



        


        