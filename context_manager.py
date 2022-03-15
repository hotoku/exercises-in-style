class FizzBuzz:
    def __enter__(self):
        self._fizz = 1
        self._buzz = 1
        self.flag = True
        return self

    def __exit__(self, *args):
        pass

    @property
    def fizz(self):
        ret = self._fizz % 3 == 0
        if ret:
            self.flag = False
        return ret

    @property
    def buzz(self):
        ret = self._buzz % 5 == 0
        if ret:
            self.flag = False
        return ret

    def refresh(self):
        self._fizz += 1
        self._buzz += 1
        self._fizz %= 3
        self._buzz %= 5
        self.flag = True


with FizzBuzz() as fb:
    for n in range(1, 101):
        if fb.fizz:
            print("Fizz", end="")
        if fb.buzz:
            print("Buzz", end="")
        if fb.flag:
            print(n, end="")
        print()
        fb.refresh()
