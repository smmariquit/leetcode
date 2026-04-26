class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a = set()
        streak = 0
        maxi = 0
        i = 0
        while i < len(s):
            l = len(a)
            curr = s[i]
            a.add(curr)
            i += 1
            m = len(a)
            if l == m:
                streak = 0
                a = set()
                i -=1
                while(s[i-1] != curr): i -=1
            else:
                streak += 1
                if streak > maxi: maxi = streak
        return maxi


        