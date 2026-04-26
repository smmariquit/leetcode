class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        arr1 = []
        arr2 = []
        for i in s:
            arr1.append(i)
        for i in t:
            arr2.append(i)
        arr1.sort()
        arr2.sort()
        if arr1 == arr2:
            return True
        return False

        