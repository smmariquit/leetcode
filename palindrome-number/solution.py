class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        length = len(num)
        j = 0
        if x < 0:
            return False
        if length == 1:
            return True
        for i in range(0,length):
            if num[i] == num[length-i-1]:
                j=j+1
            if j == length-1:
                return True
        return False

        