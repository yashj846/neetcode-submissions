class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) -1 
        while start <= end:
            mid = (start + end)//2
            if target > matrix[mid][len(matrix[0])-1]: 
                start = mid + 1
            elif target < matrix[mid][0]:
                end = mid -1
            elif (target == matrix[mid][0]) or (target == matrix[mid][len(matrix[0])-1]):
                return True
            elif matrix[mid][0] < target < matrix[mid][len(matrix[0])-1]:
                break
        m = matrix[mid]
        start, end = 0, len(m) -1
        while start  <= end:
            mid = (start + end) // 2
            if target < m[mid]:
                end = mid - 1
            elif target > m[mid]:
                start = mid + 1
            else:
                return True
        return False



        # start, end = 0, len(matrix[0]) - 1
        # while start <= end:
        #     mid = (start + end) // 2
        #     if target < matrix[mid]:
                

        #     elif target > m[mid]:

        #     else:



        # row_start, row_end = 0, len(matrix)-1
        # col_start,col_end = 0, len(matrix[0]) - 1

        # while row_start <= row_end:
        #     row_mid = (row_start + row_end) // 2
        #     while col_start <= col_end:
        #         col_mid = (col_end + col_start) // 2
        #         if target < matrix[row_mid][col_mid]:
        #             col_end = col_mid - 1
        #         elif target > matrix[row_mid][col_mid]:
        #             col_start = col_mid + 1
        #         else:
        #             return True
        #     if target < matrix[row_mid][col_mid]:
        #         row_end = row_mid - 1
        #     elif target > matrix[row_mid][col_mid]:
        #         row_start = row_mid + 1
        #     else:
        #         return True 
        # return False
            
    


        
        