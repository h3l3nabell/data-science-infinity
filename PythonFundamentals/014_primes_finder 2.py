"""
  Primes Finder Mini Project
"""
# We know that most primes are in the lower part of the number set, so
# lets use this to drastically reduce our numbers to check before we start
# preparation_limit = 20

# if primes_limit < preparation_limit:
#     preparation_limit = primes_limit

# for i in range(1, preparation_limit):
#     multiples = set(range(i*2, preparation_limit, i))

# # primes that we have found
# primes_list = []
# check_count = 0

# while there are still items in the numbers_to_check set


# Version 7

import time

# test
primes_limit = 20
range_limit = primes_limit + 1
numbers_to_check = set(range(2, range_limit))
primes_list = []
multiples_checked = set()

#possibleprime = numbers_to_check.pop()
possibleprime = 0

# loop starts here
if possibleprime > 0:
    lastprime = possibleprime

# possibleprime = numbers_to_check.pop()

if possibleprime in multiples_checked:
    # we don't need to calculate its multiples again
    possibleprime = numbers_to_check.pop()
    numpers_to_check.add(lastprime)
elif possibleprime > (primes_limit / possibleprime):
    # we know this has no higher multiples within the range
    multiples_checked.add(possibleprime)
    # but it still might be a multiple itself so we put it back in the set.
    possibleprime = numbers_to_check.pop()
    numbers_to_check.add(lastprime)
else:
    # possible prime is less than limit / possible prime so calc multiples
    multiples = set(range(possibleprime*2, range_limit, possibleprime))
    if len(multiples) > 0:
        numbers_to_check.difference_update(multiples)
        multiples_checked.difference_update(multiples)
    multiples_checked.add(possibleprime)
    possibleprime = numbers_to_check.pop()
    numbers_to_check.add(lastprime)


def find_primes_under(primes_limit=20):
    start = time.time()

    range_limit = primes_limit + 1
    numbers_to_check = set(range(2, range_limit))
    primes_list = []
    multiples_checked = set()

    lastprime = 0
    lastprimeset = set()

    while numbers_to_check:
        if lastprime > 0:
            lastprimeset = {lastprime}

        # we know the lowest number from the numbers to check set is a prime
        # so we pop the first number from the list, and then check if we
        # have eliminated it from our set check
        possibleprime = numbers_to_check.pop()
        lastprime = possibleprime

        if possibleprime > (primes_limit / possibleprime):
            # we know this has no higher multiples within the range
            multiples_checked_list.

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
