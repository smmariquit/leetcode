class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        products = {}
        n = len(nums)
        count = 0
        for i in range(0, n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                if product not in products:
                    products[product] = 1
                else:
                    products[product] += 1
        for product_count in products.values():
            count += product_count * (product_count - 1)  # Number of pairs for each product
        return count * 4 # Since each tuple has 4 elements, multiply the count by 4