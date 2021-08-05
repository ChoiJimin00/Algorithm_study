## 리스트 에서 append, pop - O(1)
## remove, index - O(n) # 검색 필요

# A.append(x) : 리스트 A 끝에 항목 x 추가 - O(1)
color = ['green','blue']#
color.append('purple')
print(color)

# A.extend(c) : 반복 가능한 모든 항목 c를 리스트에 추가 - O(1)
color = ['green','blue']
color.extend('purple')
print(color)

# A.insert(i,x) : 리스트 A의 인덱스 위치 i에 항목 x 삽입 - O(n)
color = ['green','blue']
color.insert(0,'purple')
print(color)

# a.remove(x) : 리스트 A의 항목 x 제거 / x가 없는 경우 ValueError 예외 발생 - O(n)
color = ['green','blue']
color.remove('blue')
print(color)

# A.pop(x) : 리스트 A에서 인덱스 x에 있는 항목 제거, 반환 - O(n)
# x 지정 하지 않으면 리스트 맨 끝 항목 제거, 반환
color = ['green','blue','red']
color.pop(1)
print(color)

color.pop()
print(color)

# del : 리스트 인덱스를 지정하여 특정 항목 삭제 - O(n)
numbers = [1,2,10,-1,8]
del numbers[3]
print(numbers)

# A.index(x) : 리스트 A에서 항목 x의 인덱스 반환 - O(n)
color = ['green','blue','purple']
print(color.index('purple'))

# A.count(x): 리스트 A에 항목 x가 몇개 들어있는지 개수 반환 - O(n)
color = ['purple','green','blue','purple']
print(color.count('purple'))

# A.sort(key, reverse)  / reverse = False(default) ; 오름차순 정렬 - O(n log n)
#  reverse = True - 내림차순 정렬

eng = ['city','butterfly','density','air']
eng.sort()
print(eng)
eng.sort(reverse=True)
print(eng)

# A.reverse() : 리스트 A의 항목들 반전 - O(n)
eng = ['city','butterfly','density','air']
eng.reverse()
print(eng)

## list comprehension :  반복문의 표현식 - O(n)
# 가독성을 위해 단순한 경우에만 사용하는 것이 좋음 !!!!
# [ 항목 for 항목 in 반복 가능한 객체 ]
# [ 표현식 for 항목 in 반복 가능한 객체 ]
# [ 표현식 for 항목 in 반복 가능한 객체 if 조건문 ]

n = [cnt for cnt in range(0,2000) if cnt % 250 == 0]
print(n)

sq = [i**2 for i in range(10)]
print(sq)

words = 'umm now is 11:11pm and simsim hae'.split()
dic = [ [w.capitalize(), w.upper(), w.lower(), len(w)] for w in words]
for i in dic:
    print(i)
