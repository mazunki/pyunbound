#!/usr/bin/env python
from abc import ABC, abstractmethod
from typing import Optional, Callable
import copy
import time
import sys

class Unbound(ABC):
    def __init__(self, start: int=1, end: Optional[int]=None):
        self.start, self.end = start, end

    @abstractmethod
    def __iter__(self):
        self.num = self.start
        while self.end is None or self.num < self.end:
            yield self.num
            self.num += 1

    @property
    def naturals(self):
        return Unbound.__iter__(self)

    def __add__(self, other):
        return DerivedUnbound.derive(self, lambda v: v+other, expr=f"+{other}")

    def __sub__(self, other):
        return DerivedUnbound.derive(self, lambda v: v-other, expr=f"−{other}")

    def __mul__(self, other):
        return DerivedUnbound.derive(self, lambda v: v*other, expr=f"×{other}")

    def __truediv__(self, other):
        return DerivedUnbound.derive(self, lambda v: v/other, expr=f"÷{other}")

    def __floordiv__(self, other):
        return DerivedUnbound.derive(self, lambda v: v//other, expr=f"//{other}")

    def __pow__(self, other):
        return DerivedUnbound.derive(self, lambda v: v**other, expr=f"**{other}")

    def __str__(self):
        return f"{self.__class__.__name__}{self.domain_str}"

    @property
    def domain_str(self):
        s = f"{self.start if self.start != 1 else ''}"
        e = f"{self.end if self.end else ''}"
        domain = f"{s}{'..' if s or e else ''}{e}"
        return f"({domain})" if domain else ''

    def __enter__(self):
        self._start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self._end_time = time.time()
        self._execution_time = self._end_time - self._start_time
        del self._start_time
        del self._end_time
        self.on_completion()
        if exc_type is KeyboardInterrupt:
            return True

    def on_completion(self):
        self.end = self.num
        # \r to remove ^C
        print(f"\r{self}: {self._execution_time}s", file=sys.stderr)


class DerivedUnbound(Unbound):
    def __init__(self, base: Unbound, op: Callable, expr: str=""):
        if base is None:
            raise ValueError("base_class must be an iterable")

        self.base = copy.copy(base)
        self.operations: list[Callable] = [op]
        self.expressions: list[str] = [expr]
        super().__init__(start=base.start, end=base.end)

    def __str__(self):
        operation_str = ' → '.join(self.expressions)
        return "<DerivedUnbound[{}{}]: {}>".format(self.base, self.domain_str, operation_str)

    def __iter__(self):
        self.num = self.start
        generator = iter(self.base)
        for operation in self.operations:
            generator = map(operation, generator)

        for self.num, value in enumerate(generator, start=self.start):
            yield value

    @classmethod
    def derive(cls, base: Unbound, op: Callable, expr: str=""):
        if isinstance(base, DerivedUnbound):
            derived = copy.deepcopy(base)
            derived.operations.append(op)
            derived.expressions.append(expr)
            return derived
        else:
            return cls(base=base, op=op, expr=expr)

