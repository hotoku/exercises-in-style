from abc import ABC, abstractmethod
from dataclasses import dataclass


class Speakable(ABC):
    @abstractmethod
    def say(n: int) -> str:
        return NotImplemented


class Fizz(Speakable):
    def say(self):
        return "Fizz"


class Buzz(Speakable):
    def say(self):
        return "Buzz"


class FizzBuzz(Speakable):
    def say(self):
        return "FizzBuzz"


@dataclass
class Number(Speakable):
    n: int

    def say(self):
        return str(n)


def factory(n: int) -> Speakable:
    if n % 15 == 0:
        return FizzBuzz()
    elif n % 3 == 0:
        return Fizz()
    elif n % 5 == 0:
        return Buzz()
    else:
        return Number(n)


for n in range(1, 101):
    print(factory(n).say())
