def add_numbers(a,b):
    """add there numbers given a, b, and c"""
    return sum([a + b])

#1. improve the perfomance of add_numbers
#2. add the doc string
def calc_diff(a,b):
    return abs(a - b)

#factorial function to compute n!
def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f
