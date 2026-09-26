class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            digits = set()
            for j in range(len(board)):
                if board[i][j] in digits:
                    return False
                elif board[i][j] != ".":
                    digits.add(board[i][j])

        for i in range(len(board)):
            digits = set()
            for j in range(len(board)):
                if board[j][i] in digits:
                    return False
                elif board[j][i] != ".":
                    digits.add(board[j][i])

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                digits = set()
                for m in range(3):
                    for n in range(3):
                        if board[i + m][j + n] in digits:
                            return False
                        elif board[i + m][j + n] != '.':
                            digits.add(board[i + m][j + n])
        return True


        
            

                


        