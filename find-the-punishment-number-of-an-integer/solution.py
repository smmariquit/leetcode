class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_punishable(i):
            square = str(i * i)
            n = len(square)

            def backtrack(index, current_sum):
                if index == n:
                    return current_sum == i

                for j in range(index, n):
                    substring = int(square[index:j+1])
                    if backtrack(j + 1, current_sum + substring):
                        return True
                return False

            return backtrack(0, 0)

        punishment_sum = 0
        for i in range(1, n + 1):
            if is_punishable(i):
                punishment_sum += i * i

        return punishment_sum