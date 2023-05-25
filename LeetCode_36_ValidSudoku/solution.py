#https://leetcode.com/problems/valid-sudoku/
from collections import defaultdict


def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    hashset = set()
    for i in range(9):
        for j in range(9):
            n = board[i][j]
            if n == ".":
                continue
            length = len(hashset)
            hashset.add(n + " in Row " + str(i))
            if len(hashset) == length: return False
            hashset.add(n + " in Column " + str(j))
            if len(hashset) == length + 1: return False
            hashset.add(n + " in Box " + str(i//3) + "-" + str(j//3))
            if len(hashset) == length + 2: return False
    return True

        
    

        
     




def main():
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print("Test1: ")
    res = isValidSudoku(board)
    print("Result", res)

if __name__ == "__main__":
    main()