from sortedcontainers import SortedList  # Install: pip install sortedcontainers

class NumberContainers:

    def __init__(self):
        self.index_map = {}
        self.number_map = {}

    def change(self, index, number):
        if index in self.index_map:
            old_number = self.index_map[index]
            self.number_map[old_number].remove(index)
            if not self.number_map[old_number]:
                del self.number_map[old_number]

        self.index_map[index] = number
        if number not in self.number_map:
            self.number_map[number] = SortedList()  # Use SortedList
        self.number_map[number].add(index)  # SortedList handles insertion in sorted order

    def find(self, number):
        if number not in self.number_map:
            return -1
        else:
            return self.number_map[number][0]