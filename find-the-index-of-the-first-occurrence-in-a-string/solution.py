class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: # Edge case: needle or haystack is empty
            return 0

        haystack_iterator = 0 # Set a haystack iterator
        while haystack_iterator <= len(haystack) - len(needle): # Ensure we don't go out of bounds. If lumampas na sa haystack length minus needle length minus one, impossible na
            match = True # By default, match
            for needle_iterator in range(len(needle)): # For each letter in haystack, iterate through all needle letters
                if haystack[haystack_iterator + needle_iterator] != needle[needle_iterator]: # If may isang char na hindi equal, matic next haystack leeter na
                    match = False
                    break
            if match: # If mnagmatch, yay
                return haystack_iterator
            haystack_iterator += 1
        return -1