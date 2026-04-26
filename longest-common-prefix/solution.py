class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        x = min([len(strs[x]) for x in range(len(strs))])
        for i in range(x):
            arr = []
            for j in range(len(strs)):
                arr.append(strs[j][:i+1])
            if len(set(arr)) == 1:
                prefix = arr[0]
        return prefix
