class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digit_sum_map = {}  # Store the largest two numbers for each digit sum
        max_sum = -1

        for num in nums:
            digit_sum = self.get_digit_sum(num)

            if digit_sum not in digit_sum_map:
                digit_sum_map[digit_sum] = [num]  # Initialize with the first number
            else:
                digit_sum_map[digit_sum].append(num)
                digit_sum_map[digit_sum].sort(reverse=True) # Keep only the two largest

                if len(digit_sum_map[digit_sum]) > 2:
                    digit_sum_map[digit_sum].pop()

        for digit_sum in digit_sum_map:
            if len(digit_sum_map[digit_sum]) >= 2:
                max_sum = max(max_sum, digit_sum_map[digit_sum][0] + digit_sum_map[digit_sum][1])

        return max_sum

    def get_digit_sum(self, n):
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        return digit_sum