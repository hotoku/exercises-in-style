def fizzbuzz(dic):
    def decorator(f):
        def ret(n):
            s = ""
            for k, v in dic.items():
                if n % v == 0:
                    s += k
            if s:
                f(s)
            else:
                f(n)
        return ret
    return decorator


@fizzbuzz({"Fizz": 3, "Buzz": 5})
def myprint(n):
    print(n)


for n in range(1, 101):
    myprint(n)
