
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
