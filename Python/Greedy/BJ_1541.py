import sys
input = sys.stdin.readline

if __name__ == '__main__':
    equation = input().split('-')

    answer = 0
    x = sum(map(int,(equation[0].split('+'))))
    answer += x
    
    for x in equation[1:]:
        x = sum(map(int,(x.split('+'))))
        answer -= x
    
    print(answer)