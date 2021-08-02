## method 1 - O(n)
def fibo_list(n):
    fibo = []
    fibo.append(0)
    fibo.append(1)

    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo[n]

## method 2 - O(n)
def fibo_iter(n):
    if n < 2:
        return n

    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

## method 3 - O(n^2)
def fibo_recursion(n):
    if n < 2:
        return n
    return fibo_recursion(n-1)+fibo_recursion(n-2)

print(fibo_list(10))
print(fibo_iter(10))
print(fibo_recursion(10))