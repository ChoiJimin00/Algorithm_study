import sys
input = sys.stdin.readline
# recursion error 방지
sys.setrecursionlimit(10**9)

def postorder(arr):
    if len(arr) == 0:
        return
    
    left, right = [],[]
    root = arr[0] # array의 첫번째 값 => root로 설정
    
    for i in range(1, len(arr)):
        if arr[i] > root:
            left = arr[1:i]
            right = arr[i:]
            break
    else:
        left = arr[1:]
    
    # post order(후위 순회) : 왼쪽-오른쪽-루트
    postorder(left)
    postorder(right)
    print(root)

if __name__ == '__main__':
    tree = []
    while True:
        try:
            tree.append(int(input()))
        except: 
            break
        
    postorder(tree)