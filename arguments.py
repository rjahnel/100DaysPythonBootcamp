def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def calculate (n, **kwargs):
    n /= kwargs["divide"]
    n *= kwargs["multiply"]
    n += kwargs["add"]
    n -= kwargs["subtract"]
    return(n)   


print(calculate(10, add=3, multiply=5, divide=2, subtract=0) )
print(add(4, 5, 6, 7, 8, 9, 11, 13, 22))


