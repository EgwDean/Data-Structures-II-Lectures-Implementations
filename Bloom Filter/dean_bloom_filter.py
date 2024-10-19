'''
Implementation of a Bloom filter for given 
false positive probability, based on geeksforgeeks
implementation
'''

import math
from bitarray import bitarray
import mmh3

class BloomFilter(object):

    def __init__(self, set_size, false_positive_prob):

        # Size of the given set
        self.set_size = set_size

        # Probability of a false positive
        self.false_positive_prob = false_positive_prob

        # Size of the bit array
        self.bit_array_size = self.get_bit_array_size(set_size, false_positive_prob)

        # Number of hash functions
        self.num_hash = self.get_num_hash(self.bit_array_size, set_size)

        # Creation of the bit array
        self.bit_array = bitarray(self.bit_array_size)

        # Initialization of the bit array with 0s
        self.bit_array = bitarray(self.bit_array_size)

    @classmethod
    # Returns the size of the bit array
    def get_bit_array_size(self, n, P):

        m = -(n * math.log(P))/(math.log(2)**2)
        return int(m)
    
    @classmethod
    # Returns the optimal number of hash functions
    def get_num_hash(self, m, n):

        k = (m/n) * math.log(2)
        return int(k)

    # Filters given element
    def filter_element(self, element):

        # seed_val works as a seed and gives different functions
        for seed_val in range(self.num_hash):
            # Calculates bit array index
            index = mmh3.hash(element, seed_val) % self.bit_array_size
            # Sets the corresponding array bit
            self.bit_array[index] = True

    # Checks whether the element is in the set
    def check_element(self, element):

        # seed_val works as a seed and gives different functions
        for seed_val in range(self.num_hash):
            # Calculates bit array index
            index = mmh3.hash(element, seed_val) % self.bit_array_size
            # Gives result of the search
            if self.bit_array[index] == False:
                return False
            else:
                return True
