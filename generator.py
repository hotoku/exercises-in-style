def fizzbuzz():
    for n in range(1, 101):
        if n % 15 == 0:
            yield "FizzBuzz"
        elif n % 3 == 0:
            yield "Fizz"
        elif n % 5 == 0:
            yield "Buzz"
        else:
            yield str(n)


for s in fizzbuzz():
    print(s)
