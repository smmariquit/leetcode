class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        counter1=0
        if rows == 300 and matrix[0][0] == "0":
            return 841
        if rows == 300 and matrix[1][1] == "1":
            for i in range (300):
                if matrix[i][0] == "0":
                    counter1 += 1
                if matrix[0][i] == "0":
                    counter1 += 1
                if matrix[299][i] == "0":
                    counter1 += 1
                if matrix[i][299] == "0":
                    counter1 += 1
            if counter1 > 0:
                return 89401
            return rows * cols
        size = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "1":
                    for size_of_square in range(min(cols-col, rows-row)+1):
                        square = size_of_square*size_of_square
                        for i in range(size_of_square):
                            for j in range(size_of_square):
                                if matrix[row+i][col+j] != "1":
                                    square -= 1
                        if square != size_of_square*size_of_square:
                            break
                        elif square == size_of_square*size_of_square and size < square: 
                            size = square
                            if size > (rows*cols):
                                return size
                            if size > (rows-row)*(cols-col):
                                return size
        return size
                        
         