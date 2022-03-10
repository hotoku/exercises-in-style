from typing import Any, List, overload
from dataclasses import dataclass


class Fizz:
    pass


class Buzz:
    pass


@dataclass
class Int:
    n: int


@overload
def myprint(n: Int) -> None:
    ...


@overload
def myprint(n: Fizz) -> None:
    ...


@overload
def myprint(n: Buzz) -> None:
    ...


def myprint(n) -> None:
    s = ""
    if isinstance(n, Fizz):
        s += "Fizz"
    if isinstance(n, Buzz):
        s += "Buzz"
    if s:
        print(s)
    else:
        print(n.n)  # type: ignore


for n in range(1, 101):
    parents: List[Any] = [Int]
    if n % 3 == 0:
        parents.append(Fizz)
    if n % 5 == 0:
        parents.append(Buzz)
    m = type("temp", tuple(parents), {})(n)
    myprint(m)
