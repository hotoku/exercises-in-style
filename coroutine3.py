def coroutine(f):
    def ret(*args, **kwargs):
        cr = f(*args, **kwargs)
        next(cr)
        return cr
    return ret


@coroutine
def Myprint():
    while True:
        s = (yield)
        print(s, end="")


@coroutine
def Fizz():
    while True:
        (yield)
        myprint.send("Fizz")


@coroutine
def Buzz():
    while True:
        (yield)
        myprint.send("Buzz")


@coroutine
def Number():
    while True:
        n = (yield)
        myprint.send(str(n))


@coroutine
def Dispatch():
    while True:
        n = (yield)
        flag = True
        if n % 3 == 0:
            fizz.send(n)
            flag = False
        if n % 5 == 0:
            buzz.send(n)
            flag = False
        if flag:
            number.send(n)
        myprint.send("\n")


myprint = Myprint()
fizz = Fizz()
buzz = Buzz()
number = Number()
dispatch = Dispatch()


for n in range(1, 101):
    dispatch.send(n)
