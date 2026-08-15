from math import ceil

xy = input()
x, y = xy.split(" ")
x = int(x)
y = int(y)

def fibonacci_algorithm(x, y):
    
    d = ceil(y / x) 
    xx = (-y) % x
    yy = y * d
    
    print(d, end = " ")

    if xx > 1:
        fibonacci_algorithm(xx, yy)
    elif xx == 1:
        print(yy)
    else:
        print()
        
fibonacci_algorithm(x, y)
