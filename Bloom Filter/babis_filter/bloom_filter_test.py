# Import the BloomFilter class
from bloom_filter import BloomFilter  # Ensure this matches the filename where the class is defined

# Testing BloomFilter with a specific false positive probability
false_positive_prob = 0.05

# Elements to be added to the Bloom filter
existent_strings = ["tiger", "sunshine", "ocean", "galaxy", "chocolate", "maple", "butterfly", "volcano", "whisper", "nebula"]

# Elements not added, for testing false positives
non_existent_strings = ["theo", "dean", "babis (pookie)"]

# Initialize Bloom filter
set_size = len(existent_strings)
bloom_filter = BloomFilter(set_size, false_positive_prob)
bloom_filter.add_elements(existent_strings)  # Add all existent strings

# Test each element in both existent and non-existent lists
test_strings = existent_strings + non_existent_strings
for string in test_strings:
    if bloom_filter.contains(string):
        if string in non_existent_strings:
            print(f"'{string}' is a false positive!")
        else:
            print(f"'{string}' is probably present!")
    else:
        print(f"'{string}' is definitely not present!")
