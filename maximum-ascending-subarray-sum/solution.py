class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # Handle empty input
            return 0
        
        max_sum = 0
        current_sum = nums[0]  # Initialize with the first element
        max_sum = current_sum # Initialize max_sum

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_sum += nums[i]  # Add the current element
            else:
                max_sum = max(max_sum, current_sum)  # Update max_sum
                current_sum = nums[i]  # Reset current_sum with the current element

        max_sum = max(max_sum, current_sum) # Check after loop in case the sequence is at the end
        return max_sum
