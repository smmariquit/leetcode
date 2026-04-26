class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        additions = 0
        balance = 0
        for let in s:
            if let == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1
        return additions + balance
        