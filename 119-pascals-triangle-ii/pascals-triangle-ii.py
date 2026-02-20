class Solution:
    def getRow(self, rowIndex: int):
        row = [1]
        
        for k in range(1, rowIndex + 1):
            value = row[-1] * (rowIndex - k + 1) // k
            row.append(value)
        
        return row
        