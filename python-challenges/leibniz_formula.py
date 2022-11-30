NUM_TERMS = int(input("Enter amount of terms"))

count = 0
summation = 0

# The bigger the term, the closer to actual PI value.
# Try comparing inputs of 100 vs 1000.
while count < NUM_TERMS:
    term = ((-1) ** count) / (2*count + 1)
    summation = summation + term
    print(4 * summation)
    count += 1
