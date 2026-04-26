class ProductOfNumbers(object):

    def __init__(self):
        """
        Initializes the object with an empty stream.
        """
        self.products = [1]  # Initialize with a dummy 1 to handle k=1 cases

    def add(self, num):
        """
        Appends the integer num to the stream.
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.products = [1]  # Reset the product list if num is 0
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k):
        """
        Returns the product of the last k numbers in the current list.
        :type k: int
        :rtype: int
        """
        if k >= len(self.products):
            return 0  # Handle cases where k is larger than the number of added elements.
        return self.products[-1] // self.products[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)