class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_length = len(board[0])        

        row_seen = {i:set() for i in range(9)}
        col_seen = {i:set() for i in range(9)}
        subgrid_seen = {i:set() for i in range(9)}

        for row in range(board_length):
            for col in range(board_length):
                current_num = board[row][col]
                if current_num == '.': continue
                row_set = row_seen[row]
                col_set = col_seen[col]

                subgrid_index = (row // 3) * 3 + (col // 3)
                subgrid_set = subgrid_seen[subgrid_index]

                if current_num in row_set: return False
                if current_num in col_set: return False
                if current_num in subgrid_set: return False

                row_set.add(current_num)
                col_set.add(current_num)
                subgrid_set.add(current_num)

        
        return True






        
