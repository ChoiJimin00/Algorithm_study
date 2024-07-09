import sys
input = sys.stdin.readline

def dfs(idx,v,c): # v:모음 개수, c:자음 개수
    if len(ans) == L : 
        if v >= 1 and c >= 2:
            print(''.join(ans))
        return
    
    for i in range(idx, C):
        ans.append(word[i])
        
        if word[i] in ['a','e','i','o','u']:
            dfs(i+1,v+1,c)
        else:
            dfs(i+1,v,c+1)
        
        ans.pop()
    

if __name__ == '__main__':
    L,C = map(int, input().split())
    word = list(map(str, input().split()))
    word.sort()
    
    ans = []
    dfs(0,0,0)