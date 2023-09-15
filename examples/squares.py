#!/usr/bin/env python
from pyunbound import Unbound, DerivedUnbound
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
    try:
        with Squares(end=10*1000*1000) as squares, squares-2 as superderived:
            for sq, sd in zip(squares, superderived):
                print(f"{sq} → {sd}")
    except KeyboardInterrupt:
        exit(127)


