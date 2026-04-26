class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = 0
        for i in nums:
            if count == 0:
                candidate = i
                count += 1
                continue
            if i == candidate:
                count += 1
            if i != candidate:
                count -= 1
        return candidate

        