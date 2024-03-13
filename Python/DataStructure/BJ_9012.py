from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    
    for _ in range(N):
        order = str(input())[:-1]
        queue = deque(order[0])
        
        if order[0] == ')':
            print('NO')
            continue
        
        for i in order[1:]:
            if i == ')':
                try : 
                    if queue[-1] == '(':
                        queue.pop()
                except:
                    queue.append(i)
            else:
                queue.append(i)
        
        print('YES' if len(queue)==0 else 'NO')