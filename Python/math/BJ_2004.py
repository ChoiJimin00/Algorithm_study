# factorial의 count trailing zeroes, 소인수 분해 참고 : https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
# 참고 2 : https://tmdrl5779.tistory.com/95
n,m = map(int, input().split())

def count_two(n):
    two = 0
    
    while n != 0:
        n //= 2
        two += n
    return two

def count_five(n):
    five = 0
    
    while n != 0:
        n //= 5
        five += n
    return five

print(min(count_two(n)-count_two(m)-count_two(n-m),count_five(n)-count_five(m)-count_five(n-m)))