from dataclasses import dataclass


class Fizz:
    def say(self):
        return "Fizz"


class Buzz:
    def say(self):
        return "Buzz"


class FizzBuzz:
    def say(self):
        return "FizzBuzz"


@dataclass
class Number:
    n: int

    def say(self):
        return str(n)


def factory(n):
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
