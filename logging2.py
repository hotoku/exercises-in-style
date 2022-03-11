import logging
import sys


class FizzBuzz(logging.Filter):
    def filter(self, record):
        n = record.msg
        s = ""
        if n % 3 == 0:
            s += "Fizz"
        if n % 5 == 0:
            s += "Buzz"
        if s:
            record.msg = s
        else:
            record.msg = str(n)

        return super().filter(record)


LOGGER = logging.getLogger(__file__)
handler = logging.StreamHandler(sys.stdout)
handler.addFilter(FizzBuzz())
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.INFO)


for n in range(1, 101):
    LOGGER.info(n)
