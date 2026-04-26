class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        str = ""
        word1iter = 0
        word2iter = 0
        for i in range(0,(len(word1)+len(word2))):
            if i % 2 == 0:
                if (word1iter+1)<=len(word1):
                    str += word1[word1iter]
                    word1iter += 1
                else:
                    str += word2[word2iter]
                    word2iter += 1
            else:
                if (word2iter+1)<=len(word2):
                    str += word2[word2iter]
                    word2iter+=1
                else:
                    str += word1[word1iter]
                    word1iter+=1
        return str