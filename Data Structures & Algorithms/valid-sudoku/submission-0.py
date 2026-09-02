class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        column = {}
        matrix = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.' :
                    if board[i][j] in row:
                        return False
                    else:
                        row[board[i][j]] = 1
            row = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[j][i] != '.':
                    if board[j][i] in column:
                        return False
                    else:
                        column[board[j][i]] = 1
            column = {}

        for i in range(0,9,3):
            for j in range(0,9,3):
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] != '.':
                            if board[i+x][j+y] in matrix:
                                return False
                            else:
                                matrix[board[i+x][j+y]] = 1
                matrix = {}
        return True








        
            
        # for i range(len(board))
            
                
                # and board[i][j] in row:
                #     return False
                # else:
                #     if board[i][j] in row:
                #         row[board[i][j]] += 1
                #     else:
                #         row[board[i][j]] =1
        # print(row)
        
        # for i in range(len(board)):
        #     for j in range(len(board[i])):
        #         if board[j][i] != '.' and board[j][i] in column:
        #             return False
        #         else:
        #             if board[j][i] in column:
        #                 column[board[j][i]] += 1
        #             else:
        #                 column[board[j][i]] = 1
        # print(column)

            
        

                
            
        