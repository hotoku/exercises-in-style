def coroutine(f):
    def ret(*args, **kwargs):
        cr = f(*args, **kwargs)
        next(cr)
        return cr
    return ret


@coroutine
def fizz(dest):
    while True:
        s, n = (yield)
        if n % 3 == 0:
            s += "Fizz"
        dest.send((s, n))


@coroutine
def buzz(dest):
    while True:
        s, n = (yield)
        if n % 5 == 0:
            s += "Buzz"
        dest.send((s, n))


@coroutine
def sink():
    while True:
        s, n = (yield)
        if s:
            print(s)
        else:
            print(n)


def source(dest):
    for n in range(1, 101):
        dest.send(("", n))


source(
    fizz(
        buzz(
            sink()
        )
    )
)
