import sys
input = sys.stdin.readline

def get_prime():
    global prime_list
    
    for i in range(2, 1001):
        if prime_list[i]:
            prime_list[i+i::i] = [False] * len(prime_list[i+i::i])
        
    prime_list = list(filter(None, prime_list[2:]))
    prime_list = set(prime_list)

if __name__ == '__main__':
    prime_list = list(range(1000001))
    get_prime()
    
    while True:
        n = int(input())
        
        if n == 0:
            break
        
        for i in range(3,1001):
            if (i in prime_list) and (n-i in prime_list):
                print("%d = %d + %d" %(n,i,n-i))
                break
        else:
            print("Goldbach's conjecture is wrong.")