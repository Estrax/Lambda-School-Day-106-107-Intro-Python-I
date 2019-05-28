# using Sieve of Erastothenes

import math


def is_prime(num):
    numbers = [[x, True] for x in range(2, num+1)]
    print(numbers)
    for x in numbers:
        if(x[0] >= math.sqrt(num)):
            break
        for y in numbers:
            if y[0] % x[0] == 0:
                y[1] = False
    return numbers[-1][1]


print(is_prime(32))
