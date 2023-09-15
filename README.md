
# pyunbound

so uh, i guess we haskellified python by making it support infinite sets lol lmao

## usage 

check the example implementations, or just follow this template:

```python
from pyunbound import Unbound

class Squares(Unbound):
    def __init__(self):
        super().__init__()

    def __iter__(self):
        for num in self.naturals:
            yield num**2
```

and then you can use your class as follows, for instance:

```python

squares = Squares()
derived = squares - 2
superderived: squares*3

for sq, sd in zip(squares, superderived):
    print(f"{sq} => {sd}")
```

