import sys
input = sys.stdin.readline

def get_max(tree, N, C, W):
    max_money = 0
    for i in range(1,max(tree)+1):
        money = 0
        
        for j in tree:
            tree_cnt, remain = divmod(j,i)
            
            if remain:
                expense = tree_cnt * C
            else:
                expense = (tree_cnt-1) * C
                
            target = tree_cnt * W * i - expense
            if target < 0:
                continue
            money += target
            
        if money > max_money:
            max_money = money
    
    return max_money
            

if __name__ == '__main__':
    N,C,W = map(int, input().split())
    tree = [int(input()) for _ in range(N)]
    print(get_max(tree, N,C,W))