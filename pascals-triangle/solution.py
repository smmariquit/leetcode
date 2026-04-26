class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascals = []
        for i in range(numRows):
            if i == 0:
                pascals.append([1])
            if i == 1:
                pascals.append([1,1])
            elif i >= 2:
                row = [1]
                for j in range(i-1):
                    row.append(pascals[i-1][j]+pascals[i-1][j+1])
                row.append(1)
                pascals.append(row)
        return pascals
            