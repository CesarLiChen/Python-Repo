FIB_RANGE = 100

n1 = 0
n2 = 1
fib_seq = 0

print(n1)
print(n2)
while n1 < FIB_RANGE:
    fib_seq = n1 + n2
    n1 = n2
    n2 = fib_seq
    print(fib_seq)
