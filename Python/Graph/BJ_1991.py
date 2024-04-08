import sys
input = sys.stdin.readline

def preorder(root):
    global tree
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
        
def inorder(root):
    global tree
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
    
def postorder(root):
    global tree
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root


if __name__ == '__main__':
    N = int(input())
    tree = {}
    
    for i in range(N):
        root,left,right = input().split()
        tree[root] = [left, right]
        
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')