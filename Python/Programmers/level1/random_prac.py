import random

values = [1,2,3,4]
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

print(random.sample(values, 2))
print(random.sample(values, 3))

# value 리스트를 섞음
random.shuffle(values)
print(values)

# 0~10의 임의의 정수 생성
print(random.randint(0, 10))
print(random.randint(0, 10))


## list
li = [2,1,6,4]
li.sort()
print(li)
li.sort(reverse=True)
print(li)
li.reverse()
print(li)

mm = [1,2,3]
print(mm.index(2))

tt = [1,4,7,2,7]
print(tt.count(7))
tt.insert(0,100)
print(tt)
tt.remove(7)
print(tt)

## 문자열 관련 함수
# count 특정 문자수 반환
# find 특정 문자 위치 반환
# join 문자 사이에 특정 문자 삽입
# upper 대문자 변환
# lower 소문자 변환
# replace 문자 치환
# split 문자열 분리
#  strip 양쪽 공백 제거

aa = "hello"
print(aa.count('l'))
print(aa.replace('l','k'))
phone = '010-3585-5166'
print(phone.split('-'))



