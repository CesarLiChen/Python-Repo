# Multiples of 3 -> Fizz
# Multiples of 5 -> Buzz
# Multiples of both -> FizzBuzz

out = 1
while out < 101:
    if out % 3 == 0 and out % 5 == 0:
        print(f"{out} -> FizzBuzz")
    elif out % 3 == 0 and not out % 5 == 0:
        print(f"{out} -> Fizz")
    elif out % 5 == 0 and not out % 3 == 0:
        print(f"{out} -> Buzz")
    else:
        print(str(out))
    out += 1
