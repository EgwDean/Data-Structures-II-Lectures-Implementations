'''
Implementation of a Bloom filter for given 
false positive probability, based on geeksforgeeks
implementation
'''


import math
from bitarray import bitarray
import mmh3

class BloomFilter:
    def __init__(self, set_size, false_positive_prob):
        self.set_size = set_size
        self.false_positive_prob = false_positive_prob
        self.bit_array_size = self._calculate_bit_array_size(set_size, false_positive_prob)
        self.num_hash = self._calculate_num_hash(self.bit_array_size, set_size)
        self.bit_array = bitarray(self.bit_array_size)
        self.bit_array.setall(0)  # Initialize all bits to 0

    @staticmethod
    def _calculate_bit_array_size(n, p):
        """Calculate the optimal size of bit array `m` for given set size `n` and false positive probability `p`."""
        return int(-(n * math.log(p)) / (math.log(2) ** 2))

    @staticmethod
    def _calculate_num_hash(m, n):
        """Calculate the optimal number of hash functions `k` based on bit array size `m` and set size `n`."""
        return int((m / n) * math.log(2))

    def add(self, element):
        """Add an element to the Bloom filter."""
        for seed in range(self.num_hash):
            index = mmh3.hash(element, seed) % self.bit_array_size
            self.bit_array[index] = True

    def add_elements(self, elements):
        """Add multiple elements to the Bloom filter."""
        for element in elements:
            self.add(element)

    def contains(self, element):
        """Check if an element is in the Bloom filter."""
        for seed in range(self.num_hash):
            index = mmh3.hash(element, seed) % self.bit_array_size
            if not self.bit_array[index]:  # If any index is 0, element is definitely not present
                return False
        return True  # Probable presence if all indexes are 1
