FIB_RANGE = 14

n1, n2 = 0, 1
fib_seq, count = 0, 0

print(n1)
print(n2)
# FIB_RANGE - 2, because we already printed
# first 2 terms.
while count < FIB_RANGE - 2:
    fib_seq = n1 + n2
    n1 = n2
    n2 = fib_seq
    print(fib_seq)
    count += 1
