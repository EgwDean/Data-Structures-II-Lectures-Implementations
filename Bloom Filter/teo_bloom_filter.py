import math
import mmh3
from bitarray import bitarray
from random import shuffle


def add(element):

    for i in range(k):
        # create digest for given item.
        # i work as seed to mmh3.hash() function
        # With different seed, digest created is different

        result = mmh3.hash(str(element), i) % m
        array[result] = 1


def check(check_lm):

    flag = 1

    for i in range(k):
        res = mmh3.hash(str(check_lm), i) % m
        if array[res] == 0:
            flag = 0
            print(f"{check_lm} is Definitely not in the list.")
            break

    if flag == 1:
        print(f"{check_lm} is Probably in the list.")


#MAIN#

n = 32 #no of items
m = int(input("Enter desired length of array (m): "))

print(f"The number of the elements (n) is: {n}\nThe length of the array (m) is: {m}")

kmin = math.ceil(0.69 * (m / n))

print(f"Recommended number of functions is: {kmin}")

k = int(input("Enter desired k: "))

p = (1 - 2.71**((-k*n)/m))**k #false positive

print(f"The probability of false positive is: {p}")

original_list = [277, 859, 727, 832, 979, 187, 265, 501, 631, 656, 351, 76, 766, 898, 769, 227, 282,
                 502, 677, 715, 1, 15, 615, 33, 823, 306, 197, 252, 749, 958, 21, 253]

search_list = [301, 500, 12, 76, 33, 15, 197]

array = [0 for _ in range(m)] #initialize array with 0

for j in original_list:
    add(j)

#print(array)

for lm in search_list:
    check(lm)


#mmh3.hash(str(integer_key), seed)
