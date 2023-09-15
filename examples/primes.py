#!/usr/bin/env python
from pyunbound import Unbound
from typing import Optional
import sys

class PrimeNumbers(Unbound):
    def __init__(self, start=1, end: Optional[int]=None):
        super().__init__(start=start, end=end)
        self._primes = set()

    def __iter__(self):
        for num in self.naturals:
            if num in self._primes:
                break
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                yield num
                self._primes.add(num)

if __name__ == "__main__":
    primes = PrimeNumbers()
    derived = primes * 2
    derived = derived - 1
    
    until = int(sys.argv[1]) 

    print(derived)
    with derived as iterator:
        for item in iterator:
            if item > until:
                break

