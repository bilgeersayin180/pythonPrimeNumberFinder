def isPrimeNumber(num):
    if (num == 2):
        print(num,"is a prime number")
        exit
    limit = num 
    numList = []
    for i in range(0,limit):
        numList.append(i)
    print(numList)
    for j in range(2,limit):
        if (num % numList[j] == 0):
            print(num,"is not a prime number")
            break
        print(j)
        if (j == limit - 1):
            print(num,"is a prime number")
        

number = int(input("Enter a positive integer: "))
print(isPrimeNumber(number))
