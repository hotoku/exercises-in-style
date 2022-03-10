from dataclasses import dataclass


@dataclass
class FizzBuzz:
    n: int

    def __str__(self):
        if self.n % 15 == 0:
            return "FizzBuzz"
        elif self.n % 3 == 0:
            return "Fizz"
        elif self.n % 5 == 0:
            return "Buzz"
        else:
            return str(self.n)


for n in range(1, 101):
    print(FizzBuzz(n))
