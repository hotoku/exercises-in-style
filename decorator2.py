def fizz(f):
    def ret(n):
        if n % 3 == 0:
            f("Fizz", n)
        else:
            f("", n)
    return ret


def buzz(f):
    def ret(s, n):
        if n % 5 == 0:
            s += "Buzz"
        if s:
            f(s)
        else:
            f(n)
    return ret


@fizz
@buzz
def myprint(n):
    print(n)


for n in range(1, 101):
    myprint(n)
