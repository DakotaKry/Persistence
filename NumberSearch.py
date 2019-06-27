import numpy


class NumberSearch:
    # Generates a list of primes to a max bound, AINT MY CODE GOTTA CHANGE, PLACE HOLDER
    def primesfrom2to(max):
        """ Input n>=6, Returns a array of primes, 2 <= p < n"""
        sieve = numpy.ones(max // 3 + (max % 6 == 2), dtype=numpy.bool)
        for i in range(1, int(max ** 0.5) // 3 + 1):
            if sieve[i]:
                k = 3 * i + 1 | 1
                sieve[k * k // 3::2 * k] = False
                sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
        return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]

    # find prime factors by testing to see if the number given is divisable by a list of primes. Probably not a very quick way
    def factors(num, bound):
        # sets primes as a list from primesform2to function
        primes = NumberSearch.primesfrom2to(bound)
        # Initates a list from generated numbers
        numbers = []
        a = num

        # If a is not already a prime then it runs a check can probably change to if
        while a not in primes:
            i = 0

            # checks to see if i has exceeded the length of the primes list
            while i <= (len(primes) - 1):

                # b is set to the prime located at index i, i is increaded by one
                b = primes[i]
                i = i + 1

                # Checks to see if a is one, since 1 is not in the primes list
                if a == 1:
                    break

                # Checks to see if b is a factor of a, if it is, b is extended to the numbers list
                if a % b == 0:
                    numbers.extend([b])
                    # a is set to the quotient
                    a = a / b
                    i = 0
            # Breaks loop when the list of primes runs out to prevent an infinite loop
            break
        if a in primes or a == 1:
            print("Factorized!")
            if a != 1:
                numbers.extend([int(a)])
                return numbers
            return numbers
        if a not in primes:
            print("Facotization failed! List too short.")