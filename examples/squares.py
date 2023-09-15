#!/usr/bin/env python
from pyunbound import Unbound
from typing import Optional
import time

class Squares(Unbound):
    def __init__(self, start=1, end: Optional[int]=None):
        super().__init__(start=start, end=end)
        self._primes = set()

    def __iter__(self):
        for num in self.naturals:
            yield num**2

if __name__ == "__main__":
    for sq in Squares(end=50):
        print(sq)
        time.sleep(0.1)

