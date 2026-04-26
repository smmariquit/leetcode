class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        def recursive(columnNumber):
            if columnNumber <= 26:
                array.append(columnNumber)
            else:
                rem = columnNumber % 26
                if rem == 0:  # Handle the 'Z' case
                    array.append(26) 
                    recursive((columnNumber // 26) - 1)
                else:
                    array.append(rem)
                    recursive(columnNumber // 26)
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        array = []
        result = ""
        recursive(columnNumber)
        print(array)
        for i in reversed(array):
            result = result + letters[i-1]
        return result
            

    