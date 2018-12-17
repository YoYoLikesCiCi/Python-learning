def fact(n):
    if n == 1 or n == 2: 
        return 1
    else:
        return fact(n-1)+f(n-2) 
a=input
b = fact(a)
print(b)

