class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = re.split(" +", s)
        for x in arr:
            if x == '':
                arr.remove(x)
        return len(arr[-1])
        