import sys
input = sys.stdin.readline
    
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

if __name__ == '__main__':
    N = int(input())
    
    people = []
    for _ in range(N):
        x,y = map(int, input().split())
        people.append([x,y])
        
    total_path = 0 
    for i in range(N-1):
        for j in range(i+1, N):
            total_path += distance(people[i][0],people[i][1],people[j][0],people[j][1])
            
    print(total_path*2/N)