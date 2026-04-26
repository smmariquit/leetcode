class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)  # Use heapq for efficient min finding
        operations = 0
        while len(nums) >= 2 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_val = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_val)  # Maintain heap property
            operations += 1

        # Check if all elements are now >= k. If not, it's impossible.
        if nums and nums[0] < k:  # Check if nums is not empty first
            return -1 # Or raise an exception, depending on requirements

        return operations
