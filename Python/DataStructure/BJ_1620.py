import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N,M = map(int, input().split())
    book = {}
    
    for i in range(1,N+1):
        monster = input().strip()
        book[str(i)] = monster
        book[monster] = str(i)
        
    for _ in range(M):
        search = input().strip()
        print(book[search])