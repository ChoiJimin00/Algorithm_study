#1978
prime_list = [2,3,5,7,11,13,17,19,23,29,31,37]

# 시간 복잡도 O(1)
def prime(a):
    for i in prime_list:
        if a == i:
            return True
        if a % i == 0:
            return False
    return True


# 시간 복잡도 O(n)
def prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    N = input()
    num_list = list(map(int, input().split()))
    cnt = 0

    for i in num_list:
        if i == 1:
            continue
        if prime(i):
            cnt += 1

    print(cnt)