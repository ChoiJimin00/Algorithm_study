import sys
input = sys.stdin.readline

def remote(N, broken):
    small = abs(N-100)

    for i in range(0,1000000,1):
        chk = 1
        i_list = [n for n in str(i)]
        
        for i_val in i_list:
            if i_val in broken:
                chk = 0
                break
           
        if chk == 1 and small > (len(i_list) + abs(N-i)):
            small = len(i_list) + abs(N-i)
                
    return small

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    
    if M == 0:
        print(min(abs(N-100),len(str(N))))
    elif M == 10:
        broken = list(map(str,input().split()))
        print(abs(N-100))
    else:
        broken = list(map(str,input().split()))
        print(remote(N, broken))