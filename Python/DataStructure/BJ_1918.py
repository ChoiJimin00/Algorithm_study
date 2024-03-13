import sys
input = sys.stdin.readline

'''
우선 순위
1) '('을 만난 경우
2) *,/ 을 만난 경우
3) 나머지 후위 연산 수행
'''

if __name__ == '__main__':
    equation = input()
    stack = []
    result = ''

    for i in equation:
        if i.isalpha():
            result += i

        elif i == '(':
            stack.append(i)

        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(i)

        elif i == '+' or i == '-' :
            while stack and (stack[-1] !='('):
                result += stack.pop()
            stack.append(i)
            
        elif i == ')':
            while stack and (stack[-1] != '('):
                result += stack.pop()
                
            stack.pop() # '(' 제거

    while stack:
        result += stack.pop()

    print(result)