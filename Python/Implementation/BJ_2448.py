import sys
input = sys.stdin.readline

def recursion(i,j,size):
    if size == 3:
        star[i][j] = '*'
        star[i+1][j-1] = star[i+1][j+1] = '*'
        for k in range(-2,3):
            star[i+2][j-k]='*'
    else:
        newsize = size//2
        recursion(i,j,newsize)
        recursion(i+newsize, j-newsize, newsize)
        recursion(i+newsize, j+newsize, newsize)

if __name__ == '__main__':
    N = int(input())
    star = [[' ']*2*N for _ in range(N)]
    
    recursion(0,N-1,N)
    
    for s in star:
        print(''.join(s))