class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        i = 0
        while i < len(s):
            current_value = roman[s[i]]
            if i + 1 < len(s):
                next_value = roman[s[i+1]]
                if current_value < next_value:
                    total += next_value - current_value
                    i += 2
                else:
                    total += current_value
                    i += 1
            else:
                total += current_value
                i += 1
        return total
