import sys
import copy
input = sys.stdin.readline

# ' ', '+', '-'의 모든 중복 조합을 찾음
def recur(arr, m):
    global formular
    if len(arr) == m:
        formular.append(copy.deepcopy(arr))
        return

    arr.append(' ')
    recur(arr,m)
    arr.pop()
    
    arr.append('+')
    recur(arr,m)
    arr.pop()
    
    arr.append('-')
    recur(arr,m)
    arr.pop()

if __name__ == '__main__':
    N = int(input())
    
    for _ in range(N):
        formular = []
        m = int(input())
        recur([],m-1)
        
        for form in formular:
            statement = ''
            for i in range(m-1):
                statement += str(i+1) + form[i]
            statement += str(m)
            if (eval(statement.replace(' ',''))) == 0:
                print(statement) 
        print()       