## stack 2개를 이용하여 풀면 O(1) 시간에 풀 수 있음
# 참고 : https://corin-e.tistory.com/entry/백준-1406-에디터-파이썬
import sys
input = sys.stdin.readline

left = list(input())[:-1]
right = []

for _ in range(int(input())):
    command = input().split()
    
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]
print(''.join(answer))