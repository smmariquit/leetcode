class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        new_array = []
        for i in digits:
            num += str(i)
        actual_num = int(num)+1
        for i in str(actual_num):
            new_array.append(int(i))
        return new_array