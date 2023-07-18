def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


x = int(input("Enter number of digits of the fibonacci series you want:"))
if x<=0:
    print("Enter a valid number")
else:
    for i in range(x):
        print(fibonacci(i))