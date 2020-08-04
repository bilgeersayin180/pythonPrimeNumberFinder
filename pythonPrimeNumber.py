def isPrime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True
number = int(input("Enter a positive integer: "))
print(isPrime(number))
