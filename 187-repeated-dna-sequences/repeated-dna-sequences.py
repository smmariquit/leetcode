class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        n = len(s)
        tmp = set()
        ans = set()
        if n<11:
            return []
        tmp.add(s[:10])
        for i in range(11,n+1):
            if s[i-10:i] in tmp:
                ans.add(s[i-10:i])
            else:
                tmp.add(s[i-10:i])
        return list(ans)
                

        