class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mat_list.append(matrix[i][j])
        
        l = 0
        r = len(mat_list)-1

        while l<=r:
            m = (l + r )//2
            if target == mat_list[m]:
                return True
            elif target < mat_list[m]:
                r = m-1
            else:
                l = m+1      
        return False



        


        