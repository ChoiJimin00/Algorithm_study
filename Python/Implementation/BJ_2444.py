import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    
    for i in range(N):
        for j in range(N-i-1):
            print(' ',end='')
        for j in range(2*i+1):
            print('*',end='')
        print()
        
    for i in range(N-1):
        for j in range(i+1):
            print(' ',end='')
        for j in range(2*(N-i)-3):
            print('*',end='')
        print()