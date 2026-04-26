class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = 0
        indices = []
        if s1 == s2: return True
        for i in range(0,len(s1)):
            if s2[i] != s1[i]: 
                count+=1
                indices.append(i)
        if count==2: 
            if s2[indices[0]] == s1[indices[1]] and s1[indices[0]] == s2[indices[1]]: return True
            else: return False   
        else: return False
        