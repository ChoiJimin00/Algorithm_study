import numpy as np

def AND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

if __name__ == '__main__':
    print("AND")
    for arr1 in [(0,0), (1,0), (0,1),(1,1)]:
        y = AND(arr1[0],arr1[1])
        print(str(arr1) + "->"+str(y))

    print("OR")
    for arr2 in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = OR(arr2[0], arr2[1])
        print(str(arr2) + " -> " + str(y))

    print("NAND")
    for arr3 in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = NAND(arr3[0], arr3[1])
        print(str(arr3) + " -> " + str(y))

    print("XOR")
    for arr4 in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(arr4[0], arr4[1])
        print(str(arr4) + " -> " + str(y))