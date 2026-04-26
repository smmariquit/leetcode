class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        count = 0
        for i in range(0,n):
            if nums[i] > nums[(i+1) % len(nums)]:
                count += 1
        return count <= 1