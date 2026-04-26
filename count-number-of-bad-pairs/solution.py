class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        good_pairs = 0
        counter = {}
        if not nums: return 0
        if len(nums) == 1: return 0
        for i in range(n):
            diff = nums[i] - i
            if diff in counter:
                good_pairs += counter[diff]  # These are good pairs
                counter[diff] += 1
            else:
                counter[diff] = 1
        total_pairs = n * (n - 1) // 2  # Total possible pairs
        bad_pairs = total_pairs - good_pairs  # Bad pairs = Total - Good
        return bad_pairs