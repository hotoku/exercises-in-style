import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout
)
for n in range(1, 101):
    if n % 15 == 0:
        logging.info("FizzBuzz")
    elif n % 3 == 0:
        logging.info("Fizz")
    elif n % 5 == 0:
        logging.info("Buzz")
    else:
        logging.info(n)
