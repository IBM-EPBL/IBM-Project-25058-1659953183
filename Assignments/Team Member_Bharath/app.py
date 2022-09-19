# Program 1:
# Given number prime or not

num = int(input("Enter a number: "))
flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

# Program 2:
# Generate odd numbers from range given using while loop

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

while (start < end):
    start += 1
    if (start % 2 == 0):
        continue
    print(start)

# Program 3
# Display prime number up to given range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
primeNum = []

for num in range(start, end + 1):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primeNum.append(num)

print(primeNum)

# Program 4
# Fibonacci series

num = int(input("Enter a range: "))


def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


if num <= 0:
    print("Enter positive integer")
else:
    for i in range(num):
        print(fibonacci(i))
