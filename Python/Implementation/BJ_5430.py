from collections import deque
import sys

input = sys.stdin.readline

def ac_function(order, arr):
    arr = deque(arr)
    check = False
    
    for _order in order:
        if _order == 'R':
            check = not check
        else:
            if check == 0:
                arr.popleft()
            else :
                arr.pop()
                
    if check:
        arr.reverse()
        
    result = '['
    while arr:
        result += arr.popleft()
        result += ','
    result = result[0:-1]
    result += ']'
    print(result)
    

T = int(input())

for _ in range(T):
    order = input()
    n = int(input())
    arr = input().split(',')
    
    if arr[0] == '[]':
        arr = deque()
    else:
        arr[0] = arr[0][1:]
        arr[n-1] = arr[n-1][:-1]
    
    if order.count('D') > n :
        print('error')
    elif order.count('D') == n :
        print('[]')
    else:
        ac_function(order, arr)