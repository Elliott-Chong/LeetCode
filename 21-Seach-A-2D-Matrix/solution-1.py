class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            middle_row = matrix[mid]
            if target > middle_row[-1]:
                top = mid + 1
            elif target < middle_row[0]:
                bottom = mid - 1
            else:
                break
            
        if top > bottom: return False
        mid = (top + bottom) // 2
        correct_row = matrix[mid]

        lp, rp = 0, COLS - 1

        while lp <= rp:
            mp = (lp + rp) // 2
            if correct_row[mp] == target: return True
            if correct_row[mp] > target:
                rp = mp - 1
            else:
                lp = mp + 1
        return False