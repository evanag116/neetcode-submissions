from typing import List

def read_integers() -> List[int]:
    ints = input().split(",")
    return [int(i) for i in ints]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
