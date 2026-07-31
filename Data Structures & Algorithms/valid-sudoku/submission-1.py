class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowcheck = set()
            for val in board[i]:
                if val == ".":
                    continue
                if val in rowcheck:
                    return False
                rowcheck.add(val)
        for col in range(9):
            colcheck = set()
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in colcheck:
                    return False
                colcheck.add(val)

        for i in range(0,8,3):
            rowstart,rowend = i,i+3
            for j in range(0,8,3):
                colstart, colend = j, j + 3  
                boxcheck = set()
                for row in range(rowstart, rowend):
                    for col in range(colstart,colend):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in boxcheck:
                            return False
                        boxcheck.add(board[row][col])
        return True
