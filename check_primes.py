from math import sqrt
from itertools import count, islice


def is_prime(n):
    # From: https://stackoverflow.com/a/27946768
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


if __name__ == "__main__":
    lists = [2, 3, 5, 7]
    multiplier = 10
    while len(lists) > 1:
        for l in list(lists):
            for i in range(10):
                new_candidate = (l* multiplier) + i
                if is_prime(new_candidate):
                    lists.append(new_candidate)
                    print(new_candidate)
            lists.remove(l)
