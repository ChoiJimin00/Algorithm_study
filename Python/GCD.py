def GCD():
    a,b = map(int, input().split())

    # 나머지가 0일때 까지
    while b != 0:
        a,b = b, a % b

    print(a)

def LCM():
    a, b = map(int, input().split())
    A, B = a, b

    while b != 0:  # 유클리드 호제법
        a, b = b, a % b

    print(A*B//a)


GCD()
LCM()