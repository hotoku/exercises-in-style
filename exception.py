class Fizz(Exception):
    pass


class Buzz(Exception):
    pass


for n in range(1, 101):
    flag = True
    for v, e in {3: Fizz(), 5: Buzz()}.items():
        try:
            if n % v == 0:
                raise e
        except Fizz:
            print("Fizz", end="")
            flag = False
        except Buzz:
            print("Buzz", end="")
            flag = False
    if flag:
        print(n, end="")
    print("")
