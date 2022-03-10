def fizzbuzz(f):
    def ret(n):
        if n % 15 == 0:
            f("FizzBuzz")
        elif n % 3 == 0:
            f("Fizz")
        elif n % 5 == 0:
            f("Buzz")
        else:
            f(n)
    return ret


@fizzbuzz
def myprint(n):
    print(n)


for n in range(1, 101):
    myprint(n)
