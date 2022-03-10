def coroutine(f):
    def ret(*args, **kwargs):
        cr = f(*args, **kwargs)
        next(cr)
        return cr
    return ret


def filter(m, word):
    @coroutine
    def ret(dest):
        cnt = 1
        while True:
            s, n = (yield)
            if cnt == 0:
                s += word
            dest.send((s, n))
            cnt += 1
            cnt %= m
    return ret


fizz = filter(3, "Fizz")
buzz = filter(5, "Buzz")


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
