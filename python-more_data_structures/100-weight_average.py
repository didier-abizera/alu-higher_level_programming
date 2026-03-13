#!/usr/bin/python3
"""Module for weight_average function"""


def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple"""
    if not my_list:
        return 0
    return sum(s * w for s, w in my_list) / sum(w for s, w in my_list)
```

---

## How it Works
```
my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]

Top:    (1*2) + (2*1) + (3*10) + (4*2) = 2+2+30+8 = 42
Bottom: 2 + 1 + 10 + 2                 = 15

42 / 15 = 2.80 ✅
