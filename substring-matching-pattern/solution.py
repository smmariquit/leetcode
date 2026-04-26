class Solution(object):
    def hasMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if p == "*":
            return True

        halves = p.split("*")

        if not halves:  # Handle empty pattern
            return not s  # s must also be empty

        if len(halves) == 1: # No * present
            return halves[0] in s

        if halves[0] == "":  # Handle cases like "*abc"
            remaining_p = "*".join(halves[1:])  # Reconstruct remaining pattern
            return self.hasMatch(s, remaining_p) # Recursion

        if halves[-1] == "":  # Handle cases like "abc*"
            remaining_p = "*".join(halves[:-1])  # Reconstruct remaining pattern
            return self.hasMatch(s, remaining_p) # Recursion

        index0 = s.find(halves[0])
        if index0 == -1:
            return False

        remaining_s = s[index0 + len(halves[0]):]

        if len(halves) == 2:
            index1 = remaining_s.find(halves[1]) # Find in the remaining string
            if index1 == -1:
                return False
            return True


        # Handle multiple *
        remaining_p = "*".join(halves[1:-1])
        
        index_current = 0
        for part in halves[1:-1]:
            index_in_remaining = remaining_s[index_current:].find(part)
            if index_in_remaining == -1:
                return False
            index_current += index_in_remaining + len(part)

        index_last = remaining_s[index_current:].find(halves[-1])
        if index_last == -1:
            return False
            
        return True