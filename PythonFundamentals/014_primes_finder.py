"""
  Primes Finder Mini Project
"""

# Version 1

import time
from ordered_set import OrderedSet

# primes_limit = 20
# range_limit = primes_limit+1
# # numbers_to_check = set(range(2, range_limit))
# numbers_to_check = OrderedSet(range(2, range_limit))

# primes_list = []

# # assumes that we are "popping" the lowest value - but we might not be
# prime = numbers_to_check.pop(0)
# # prime = min(numbers_to_check)  # I could use pop here and sort the list
# # numbers_to_check.remove(prime)
# primes_list.append(prime)

# # range(start, stop, step)
# multiples = set(range(prime*2, range_limit, prime))
# numbers_to_check.difference_update(multiples)

# print(primes_list)
# prime_count = len(primes_list)
# largest_prime = max(primes_list)
# print(f"There are {prime_count} prime numbers between 0 and {primes_limit}.")
# print(f"The largest prime is {largest_prime}.")


# Version 2


# def find_primes_under(primes_limit=20):
#     start = time.time()
#     # upper bound
#     range_limit = primes_limit+1

#     # number range to be checked
#     numbers_to_check = set(range(2, range_limit))

#     # primes that we have found
#     primes_list = []

#     # while there are still items in the numbers_to_check set
#     while numbers_to_check:
#         # we know the lowest number from the numbers to check set is a prime
#         # but we might have a problem because sets are unordered and pop in
#         # theory should be random.  In practice though, it works on my machine!
#         prime = numbers_to_check.pop()
#         primes_list.append(prime)

#         # range(start, stop, step) - we use this to find multiples of our prime
#         # and remove them from our set of numbers remaining to check
#         multiples = set(range(prime*2, range_limit, prime))
#         numbers_to_check.difference_update(multiples)

#     prime_count = len(primes_list)
#     largest_prime = max(primes_list)
#     end = time.time()
#     print(
#         f"There are {prime_count} prime numbers between 0 and {primes_limit}.")
#     print(f"The largest prime is {largest_prime}.")
#     print(f"The calculation took {end - start} seconds.")

#     return primes_list


# primes_list = find_primes_under()

# print(primes_list)


# primes_list = find_primes_under(100)
# print(primes_list)

# primes_list = find_primes_under(100000)
# print(primes_list)

# primes_list = find_primes_under(1000000)
# print(primes_list)

# Version 3


# def find_primes_under(primes_limit=20):
#     start = time.time()
#     # upper bound
#     range_limit = primes_limit + 1

#     # number range to be checked
#     numbers_to_check = set(range(2, range_limit))

#     # primes that we have found
#     primes_list = []

#     # while there are still items in the numbers_to_check set
#     while numbers_to_check:
#         # we know the lowest number from the numbers to check set is a prime
#         prime = min(sorted(numbers_to_check))
#         numbers_to_check.remove(prime)
#         primes_list.append(prime)

#         # range(start, stop, step) - we use this to find multiples of our prime
#         multiples = set(range(prime*2, range_limit, prime))

#         # here we remove them from our set of numbers remaining to check
#         numbers_to_check.difference_update(multiples)
#         # and now we need to update the list so we can reliably find the min

#     prime_count = len(primes_list)
#     largest_prime = max(primes_list)
#     end = time.time()
#     print(
#         f"There are {prime_count} prime numbers between 0 and {primes_limit}.")
#     print(f"The largest prime is {largest_prime}.")
#     print(f"The calculation took {end - start} seconds.")

#     return primes_list


# primes_list = find_primes_under()

# print(primes_list)


# primes_list = find_primes_under(100)
# print(primes_list)

# primes_list = find_primes_under(1000)
# print(primes_list)

# primes_list = find_primes_under(100000)
# print(primes_list)

# primes_list = find_primes_under(1000000)
# print(primes_list)

# Version 4


# def find_primes_under(primes_limit=20):
#     start = time.time()
#     # upper bound
#     range_limit = primes_limit + 1

#     # number range to be checked
#     numbers_to_check = OrderedSet(range(2, range_limit))

#     # primes that we have found
#     primes_list = []

#     # while there are still items in the numbers_to_check set
#     while numbers_to_check:
#         # Using an ordered set we should be able to pop them.
#         prime = numbers_to_check.pop(0)
#         primes_list.append(prime)

#         # range(start, stop, step) - we use this to find multiples of our prime
#         multiples = set(range(prime*2, range_limit, prime))

#         # here we remove them from our set of numbers remaining to check
#         numbers_to_check.difference_update(multiples)

#     prime_count = len(primes_list)
#     largest_prime = max(primes_list)
#     end = time.time()
#     print(
#         f"There are {prime_count} prime numbers between 0 and {primes_limit}.")
#     print(f"The largest prime is {largest_prime}.")
#     print(f"The calculation took {end - start} seconds.")

#     return primes_list


# primes_list = find_primes_under()

# print(primes_list)


# primes_list = find_primes_under(100)
# print(primes_list)

# primes_list = find_primes_under(100000)
# print(primes_list)

# primes_list = find_primes_under(1000000)
# print(primes_list)


# Version 5
numbers_to_check_list = [2]
numbers_to_check_list2 = list(range(3, 50, 2))
numbers_to_check_list.extend(numbers_to_check_list2)


def find_primes_under(primes_limit=20):
    start = time.time()
    # upper bound
    range_limit = primes_limit + 1

    # number range to be checked - we need both a list and a set for
    # this experiment
    numbers_to_check_list = list(range(3, range_limit, 2))
    numbers_to_check_excluding_multiples_set = set(numbers_to_check_list)

    # primes that we have found
    primes_list = []

    # while there are still items in the numbers_to_check set
    while numbers_to_check_excluding_multiples_set:
        # we know the lowest number from the numbers to check set is a prime
        # so we pop the first number from the list, and then check if we
        # have eliminated it from our set check
        prime = numbers_to_check_list.pop(0)
        if prime not in numbers_to_check_excluding_multiples_set:
            # we don't need to check this, it's been excluded already
            continue
        else:
            primes_list.append(prime)
            numbers_to_check_excluding_multiples_set.remove(prime)

        # range(start, stop, step) - we use this to find multiples of our prime
        # within the specified range
        multiples = set(range(prime*2, range_limit, prime))

        # here we remove them from our set of numbers remaining to check
        numbers_to_check_excluding_multiples_set.difference_update(multiples)
        # and now we need to update the list so we can reliably find the min
        numbers_to_check_list = list(numbers_to_check_excluding_multiples_set)

    prime_count = len(primes_list)
    largest_prime = max(primes_list)
    end = time.time()
    print(
        f"There are {prime_count} prime numbers between 0 and {primes_limit}.")
    print(f"The largest prime is {largest_prime}.")
    print(f"The calculation took {end - start} seconds.")

    return primes_list


primes_list = find_primes_under()

print(primes_list)


primes_list = find_primes_under(100)
print(primes_list)

primes_list = find_primes_under(1000)
print(primes_list)

primes_list = find_primes_under(100000)
print(primes_list)

primes_list = find_primes_under(1000000)
print(primes_list)


# Version 6
primes_limit = 100
range_limit = primes_limit + 1

# number range to be checked
numbers_to_check = set(range(2, range_limit))
print(len(numbers_to_check))
print(numbers_to_check)

# We know that most primes are in the lower part of the number set, so
# lets use this to drastically reduce our numbers to check before we start
preparation_limit = 20

if primes_limit < preparation_limit:
    preparation_limit = primes_limit

all_multiples = set()
for i in list(range(2, preparation_limit)):
    print(i)
    multiples = set(range(i*2, range_limit, i))
    print(multiples)
    all_multiples.update(multiples)

print(len(all_multiples))
print(len(numbers_to_check))
print(all_multiples)
numbers_to_check.difference_update(all_multiples)
print(len(numbers_to_check))
print(numbers_to_check)


def find_primes_under(primes_limit=20):
    start = time.time()
    # upper bound
    range_limit = primes_limit + 1

    # number range to be checked
    numbers_to_check = set(range(2, range_limit))

    # We know that most primes are in the lower part of the number set, so
    # lets use this to drastically reduce our numbers to check before we start
    preparation_limit = 20

    if primes_limit < preparation_limit:
        preparation_limit = primes_limit

    for i in range(1, preparation_limit):
        multiples = set(range(i*2, preparation_limit, i))

    # primes that we have found
    primes_list = []
    check_count = 0

    # while there are still items in the numbers_to_check set
    while len(numbers_to_check) > check_count:
        # we know the lowest number from the numbers to check set is a prime
        # so we pop the first number from the list, and then check if we
        # have eliminated it from our set check
        possibleprime = numbers_to_check.pop()

        # range(start, stop, step) - we use this to find multiples of our prime
        # within the specified range
        multiples = set(range(possibleprime*2, range_limit, possibleprime))

        # here we remove them from our set of numbers remaining to check
        if len(multiples) > 0:
            numbers_to_check.difference_update(multiples)

        # add the popped value back in, to go round again.

    prime_count = len(primes_list)
    largest_prime = max(primes_list)
    end = time.time()
    print(
        f"There are {prime_count} prime numbers between 0 and {primes_limit}.")
    print(f"The largest prime is {largest_prime}.")
    print(f"The calculation took {end - start} seconds.")

    return primes_list


primes_list = find_primes_under()

print(primes_list)


primes_list = find_primes_under(100)
print(primes_list)

primes_list = find_primes_under(1000)
print(primes_list)

primes_list = find_primes_under(100000)
print(primes_list)

primes_list = find_primes_under(1000000)
print(primes_list)


# Version 7

def find_primes_under(primes_limit=20):
    start = time.time()
    # upper bound
    range_limit = primes_limit + 1

    # number range to be checked
    numbers_to_check = set()
    numbers_to_check.add(2)
    numbers_to_check.update(set(range(3, range_limit, 2)))

    # we don't need to check multiples beyond the half way mark, there wont be
    # any multiples in the range after that, they won't fit!
    # so let's cut down our work a bit more.
    # Also, after 2, we only need to check odd numbers for multiples
    # But we have already eliminated the even numbers after 2
    # before we start, so we'll start checking @3
    multiples_to_check_list = list(range(3, int(range_limit / 2), 2))

    # We eliminate multiples of our list
    for i in multiples_to_check_list:
        # range(start, stop, step) - we use this to find multiples of our prime
        # within the specified range, and seek & destroy
        multiples = set(range(i*2, range_limit, i))

        # here we remove them from our set of numbers remaining to check
        if len(multiples) > 0:
            numbers_to_check.difference_update(multiples)

    # once we have eliminated the impossible, all that remains, however
    # improbable, must be a prime.
    prime_count = len(numbers_to_check)
    largest_prime = max(numbers_to_check)
    end = time.time()
    print(
        f"There are {prime_count} prime numbers between 0 and {primes_limit}.")
    print(f"The largest prime is {largest_prime}.")
    print(f"The calculation took {end - start} seconds.")

    return numbers_to_check


primes = find_primes_under()
print(primes)


primes = find_primes_under(100)
print(primes)

primes = find_primes_under(1000)
print(primes)

primes = find_primes_under(100000)
print(primes)

primes = find_primes_under(1000000)
print(primes)

# Version 8


def find_primes_under(primes_limit=20):
    start = time.time()
    # upper bound
    range_limit = primes_limit + 1

    # number range to be checked
    numbers_to_check = set()
    numbers_to_check.add(2)
    numbers_to_check.update(set(range(3, range_limit, 2)))

    # we'll start checking odd numbers @ 3
    multiples_to_check_list = list(range(3, int(range_limit / 2), 2))

    # We eliminate multiples of our list
    for i in multiples_to_check_list:
        # but if our number i is greater than the range limit / i, we cannot
        # find any multiples more, because they will already
        # have been eliminated.  So we can stop. Our work is done.
        if i > range_limit / i:
            break

        multiples = set(range(i*2, range_limit, i))

        # here we remove them from our set of numbers remaining to check
        if len(multiples) > 0:
            numbers_to_check.difference_update(multiples)

    # once we have eliminated the impossible, all that remains, however
    # improbable, must be a prime.
    prime_count = len(numbers_to_check)
    largest_prime = max(numbers_to_check)
    end = time.time()
    print(
        f"There are {prime_count} prime numbers between 0 and {primes_limit}.")
    print(f"The largest prime is {largest_prime}.")
    print(f"The calculation took {end - start} seconds.")

    return numbers_to_check


primes = find_primes_under()
print(primes)


primes = find_primes_under(100)
print(primes)

primes = find_primes_under(1000)
print(primes)

primes = find_primes_under(100000)
print(primes)

primes = find_primes_under(1000000)
print(primes)
