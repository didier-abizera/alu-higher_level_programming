#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""
    return sum(set(my_list))
```

---

## How it Works
```
my_list = [1, 2, 3, 1, 4, 2, 5]

set(my_list) → {1, 2, 3, 4, 5}  # removes duplicates
sum({1, 2, 3, 4, 5}) → 15 
