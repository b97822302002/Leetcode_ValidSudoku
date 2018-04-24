class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range (0, 9):
            if self.row(board, i) == False:
                return False
        for j in range (0, 9):
            if self.col(board, j) == False:
                return False
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                if self.squ(board, i, i+3, j, j+3) == False:
                    return False

        return True

    def row(self, board, i):
        checkList = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for j in range(0, 9):
            if board[i][j] == ".":
                continue
            elif board[i][j] in checkList:
                checkList.remove(board[i][j])
            else:
                return False
        return True

    def col(self, board, j):
        checkList = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(0, 9):
            if board[i][j] == ".":
                continue
            elif board[i][j] in checkList:
                checkList.remove(board[i][j])
            else:
                return False
        return True

    def squ( self, board, istart, iend, jstart, jend ):
        checkList = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(istart, iend):
            for j in range(jstart, jend):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in checkList:
                    checkList.remove(board[i][j])
                else:
                    return False
        return True

print(Solution().isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))
    