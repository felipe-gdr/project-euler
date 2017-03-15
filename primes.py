def initialize_primes(max_prime):
    """
    Initializes the list of prime numbers using Sieve of Erastosthenes.

    source: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    Parameters:
      max_prime - no initialized prime number will be higher than this parameter
    """
    primes, sieve = [], [True] * (max_prime + 1)
    for p in range(2, max_prime + 1):
        if sieve[p]:
           primes.append(p)
           for i in range(p * p, max_prime + 1, p):
               sieve[i] = False
    return primes

print initialize_primes(100)
