#!/usr/bin/env python
from abc import ABC, abstractmethod
from typing import Optional, Callable
import copy

class Unbound(ABC):
    def __init__(self, start: int=1, end: Optional[int]=None):
        self.start, self.end = start, end

    @abstractmethod
    def __iter__(self):
        num = self.start
        while self.end is not None and num < self.end:
            yield num
            num += 1

    @property
    def naturals(self):
        return Unbound.__iter__(self)

    def __add__(self, other):
        return DerivedUnbound.derive(self, lambda v: v+other, expr=f"+{other}")

    def __sub__(self, other):
        return DerivedUnbound.derive(self, lambda v: v-other, expr=f"-{other}")

    def __mul__(self, other):
        return DerivedUnbound.derive(self, lambda v: v*other, expr=f"*{other}")

    def __truediv__(self, other):
        return DerivedUnbound.derive(self, lambda v: v/other, expr=f"/{other}")

    def __floordiv__(self, other):
        return DerivedUnbound.derive(self, lambda v: v//other, expr=f"//{other}")

    def __pow__(self, other):
        return DerivedUnbound.derive(self, lambda v: v**other, expr=f"**{other}")

    def __str__(self):
        return f"{self.__class__.__name__}({self.start}..{self.end or ''})"

class DerivedUnbound(Unbound):
    def __init__(self, base: Unbound, op: Callable, expr: str=""):
        if base is None:
            raise ValueError("base_class must be an iterable")

        self.base = copy.copy(base)
        self.operations: list[Callable] = [op]
        self.expressions: list[str] = [expr]
        super().__init__(start=base.start, end=base.end)

    def __str__(self):
        operation_str = ' -> '.join(self.expressions)
        return f"<DerivedUnbound[{self.base}]: {operation_str}>"

    def __iter__(self):
        generator = iter(self.base)
        for operation in self.operations:
            generator = map(operation, generator)
        return generator

    @classmethod
    def derive(cls, base: Unbound, op: Callable, expr: str=""):
        if isinstance(base, DerivedUnbound):
            derived = copy.deepcopy(base)
            derived.operations.append(op)
            derived.expressions.append(expr)
            return derived
        else:
            return cls(base=base, op=op, expr=expr)
