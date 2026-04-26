class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or s.isdigit():  # Base cases
            return ""

        for i, char in enumerate(s):
            if char.isdigit():
                left_index = i - 1
                while left_index >= 0 and s[left_index].isdigit():
                    left_index -= 1
                # Remove the digit and the closest non-digit to its left
                return self.clearDigits(s[:max(0, left_index)] + s[i + 1:])
        return s  # No digits found, return the original string
            
