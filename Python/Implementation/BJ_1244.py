import sys
input =  sys.stdin.readline

def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


if __name__ == '__main__':
    N = int(input())
    switch = [-1]+list(map(int, input().split()))
    
    person = int(input())
    for i in range(person):
        s, num = map(int, input().split())
        
        if s == 1:
            for i in range(num, N+1, num):
                change(i)
        else:
            change(num)
            for k in range(N//2):
                if num-k < 1 or num+k > N:
                    break
                if switch[num-k] == switch[num+k] :
                    change(num-k)
                    change(num+k)
                else:
                    break
        
    for i in range(1,N+1):
        print(switch[i], end = ' ')
        if i % 20 == 0:
            print()