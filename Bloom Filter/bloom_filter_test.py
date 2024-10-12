# Script for testing bloom filter

false_positive_prob = 0.05

existent_strings = [
    "tiger",
    "sunshine",
    "ocean",
    "galaxy",
    "chocolate",
    "maple",
    "butterfly",
    "volcano",
    "whisper",
    "nebula"
]

non_existent_strings = [
    "theo", 
    "dean", 
    "babis (pookie)"
]

set_size = len(existent_strings)

bloom_filter = BloomFilter(set_size, false_positive_prob)

for item in existent_strings:
    bloom_filter.filter_element(item)

test_strings = existent_strings + non_existent_strings

for string in test_strings:
    if bloom_filter.check_element(string):
        if string in non_existent_strings:
            print("'{}' is a false positive!".format(string))
        else:
            print("'{}' is probably present!".format(string))
    else:
        print("'{}' is definitely not present!".format(string))
