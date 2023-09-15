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
    squares = Squares()
    derived = squares - 2
    superderived = squares * 3

    for sq, sd in zip(squares, superderived):
        print(f"{sq} => {sd}")

