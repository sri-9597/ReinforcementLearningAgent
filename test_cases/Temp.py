from math import sqrt

class Solution:
    def primeFactors(self, n: int):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n = n / 2
        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n = n / i
        if n > 2:
            factors.add(n)
        return factors

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        primes = {2, 3, 5}
        primeFacs = self.primeFactors(n)
        if primeFacs.isSubset(primes):
            return True
        return False

print(Solution.isUgly(16))