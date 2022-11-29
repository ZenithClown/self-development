import numpy as np

def valid_rc_check(matrix : List[List[str]]) -> bool:
    # check if all the rows and columns of the sudoku
    # board is valid. convert the list into an ndarray
    # for faster element access by `[:, id]` and `[id]`
    matrix = np.array(matrix, dtype = 'str')
    
    for idx in range(9):
        # for each `idx` get the row and column values
        # also convert the data into `int` and remove blanks
        row = list(map(int, [v for v in matrix[idx] if v != "."]))
        col = list(map(int, [v for v in matrix[:, idx] if v != "."]))
        
        # check if a row/col is valid, i.e. each element
        # must be unique and thus `len == len(set)` for each
        if len(row) != len(set(row)):
            return False
        elif len(col) != len(set(col)):
            return False
        
    return True # valid


def valid_grid_check(matrix : List[List[str]]) -> bool:
    # check if all the `3x3` grid is valid/not
    matrix = np.array(matrix, dtype = 'str')
    
    for idr in range(3):
        for idc in range(3):
            value = list(matrix[(3 * idr):(3 * idr + 3), (3 * idc):(3 * idc + 3)].reshape(9))
            value = list(map(int, [v for v in value if v != "."]))
            if len(value) != len(set(value)):
                return False
            
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return valid_rc_check(board) and valid_grid_check(board)
            