# Output prime numbers starting from 2.
# A for-loop challenge.

upper_range = int(input("Please give me maximum range for searching prime numbers"))

for num in range(2, upper_range+1):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
    if isPrime:
        print(num)
