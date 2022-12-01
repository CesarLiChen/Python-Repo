# Output prime numbers starting from 2.
# A for-loop challenge.

upper_range = int(input("Please give me maximum range for searching prime numbers"))

# For each number 'num' from 2 to the user's inputted 'upper_range'
for num in range(2, upper_range+1):
    isPrime = True

    """ 
     Loop from 2 to our current number 'num'
     A prime number is divisible by 1 and itself ONLY.
     If the number was successfully divided by anything but
    1 (which is skipped in our loop) or itself, then it is 
    not a prime number.
    """
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
    # Once the second for-loop ends, if isPrime is still true
    # then we print the number.
    if isPrime:
        print(num)
