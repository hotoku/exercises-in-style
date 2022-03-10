def fizzbuzz(n):
    if n == 101:
        return
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    fizzbuzz(n+1)


fizzbuzz(1)
