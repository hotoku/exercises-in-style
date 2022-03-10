import pandas as pd

ls = pd.Series([str(n) for n in range(1, 101)],
               index=range(1, 101))
fizz = pd.Series("Fizz", index=range(3, 101, 3))
buzz = pd.Series("Buzz", index=range(5, 101, 5))
fizzbuzz = (fizz + buzz).dropna()


ls[fizz.index] = fizz
ls[buzz.index] = buzz
ls[fizzbuzz.index] = fizzbuzz
ls.map(print)
