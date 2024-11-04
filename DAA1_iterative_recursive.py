#Write a iterative program to calculate Fibonacci numbers and find its step count

COUNT = 0
x = int(input("Enter Number of Terms: "))

if x < 0:
    print("Enter valid input..")
elif x == 0:
    print(0)
elif x == 1:
    print(f"Fibonacci series up to {x}: 0")
else:
    first, sec = 0, 1
    for _ in range(x):
        print(first)
        first, sec = sec, first + sec
        COUNT +=5

print(f"Steps required using Counter fot iterative is: {COUNT}")

# Write a recursive program to calculate Fibonacci numbers and find its step count.

COUNT = 0

def recur_fibo(n):
    global COUNT
    COUNT += 1
    return n if n <= 1 else recur_fibo(n-1) + recur_fibo(n-2)

nterms = int(input("How many terms? "))

if nterms > 0:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
else:
    print("Please enter a positive integer")

print("Steps required using Counter for recursive is:", COUNT)