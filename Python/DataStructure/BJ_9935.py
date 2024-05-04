import sys
input = sys.stdin.readline

if __name__ == '__main__':
    word = input().strip()
    bomb = list(input().strip())
    n = len(bomb)
    stack = []
    
    for w in word:
        stack.append(w)        
        if stack[-n:] == bomb:
            for _ in range(n):
                stack.pop()
                
    print(''.join(stack) if stack else 'FRULA')