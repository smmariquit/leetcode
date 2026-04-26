class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = num
        while sum >= 10:
            sum = 0
            for i in str(num):
                sum += int(i)
                num = sum
        return sum
            