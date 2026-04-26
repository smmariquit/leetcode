class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        i = 0
        while i < len(nums):
            if i <= len(nums)-1 :
                if nums[i] == val:
                    counter += 0
                    nums.pop(i)
                    i -= 1
            i += 1