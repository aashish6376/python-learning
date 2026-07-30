def cube(n):
    return n*n*n
a = cube(2)
b = cube(3)
print(a+b)
def is_even(num):
    if num%2 == 0:
        print("even")
    else:
        print("odd")
is_even(8)
is_even(7)
def is_even(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
print(is_even(8))
print(is_even(87))
def greatest(a,b):
    if a>b:
        return a
    else:
        return b
print(greatest(10,20))
print(greatest(234,5457))