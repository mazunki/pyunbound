#!/usr/bin/env python
from unbound import Unbound
from typing import Optional
import time

class PrimeNumbers(Unbound):
    def __init__(self, start=1, end: Optional[int]=None):
        super().__init__(start=start, end=end)
        self._primes = set()

    def __iter__(self):
        num = self.start
        for num in self.naturals:
            if self.end is not None and num > self.end:
                break
            if num in self._primes:
                break
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                yield num

if __name__ == "__main__":
    primes = PrimeNumbers(end=50)
    derived = primes * 2
    derived2 = derived - 1
    print(primes, derived, derived2, sep="\n")

    for p1, p2, p3 in zip(primes, derived, derived2):
        print(p1, p2, p3)
        time.sleep(0.1)

