def message(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


fizzbuzz = [
    message(n)
    for n in range(1, 101)
]

print("\n".join(fizzbuzz))
