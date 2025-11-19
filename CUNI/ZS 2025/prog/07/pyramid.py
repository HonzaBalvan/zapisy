n = int(input())

def pyramid_fill(n):
    pyramid = [[None] * (n // 2 + 1) for _ in range(n // 2 + 1)]

    for i in range(n // 2 + 1):
        for j in range (n // 2 + 1):
            pyramid[i][j] = 1+i+j

    for i in range(len(pyramid)):
        pyramid[i] += pyramid[i][::-1]
        pyramid[i].pop(n // 2)
        if n % 2 == 0:
            pyramid[i].pop(n // 2)
    
    pyramid += pyramid[::-1]
    pyramid.pop(n // 2)
    if n % 2 == 0:
        pyramid.pop(n // 2)

    return pyramid

print(pyramid_fill(n))
