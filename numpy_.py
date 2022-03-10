import numpy as np

ls = np.array([str(n) for n in range(1, 101)], dtype="<U8")
ls[2::3] = "Fizz"
ls[4::5] = "Buzz"
ls[14::15] = "FizzBuzz"

print("\n".join(ls))
