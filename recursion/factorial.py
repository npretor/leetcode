

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)


f = factorial(998) # 5*4*3*2*1 factorial(n) = n * factorial(n-1)

print(f)