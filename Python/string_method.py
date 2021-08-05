# 깊은 복사
import string

peop = {'a','b','c'}
play = peop.copy()
print(peop)
play.remove('b')
print(play)
print(peop)

# 얕은 복사
peop = {'a','b','c'}
play = peop
print(peop)
play.remove('b')
print(play)
print(peop)

## 문자열 메서드
# A.join(B) : 리스트 B에 있는 모든 문자열을 하나의 단일 문자열 A로 결합

friend = ['jimin', 'nayoung', 'anne']
print(' '.join(friend))
print('**'.join(reversed(friend)))

# ljust(width, fillchar), rjust(width, fillchar) :
# A.ljust(width, fillchar) : 문자열 A '맨 처음' 부터 문자열을 포함한 길이 width 만큼 fillchar 채움
name = 'jimin'
print(name.ljust(10,'^'))
print(name.rjust(10,'^'))

# A.format(): 문자열 A에 변수 추가하거나 형식화 할때 사용
print("{} {}".format('good', 'morning'))
print('이름 : {name}, 나이 : {age}'.format(name='jella',age ='22'))
print('이름 : {name}, 나이 : {0}'.format('16',name='jella'))

name = 'jella'
print(f"my name is {name}")

## A.splitlines() : 문자열 A에 대해 줄 바꿈 문자를 기준으로 분리하여 문자열 리스트로 반환
book = '로미오\n줄리엣'
print(book.splitlines())

# A.split(t,n) : 문자열 A에서 문자열 t를 기준으로 정수 n번 만큼 분리한 문자열 리스트 반환
# n 지정 X -  대상 문자열을 t로 분리 / t 지정 X - 공백 문자로 구분한 문자열 리스트 반환
# 추가로 rsplit(t,n) lsplit(t,n) 있음
event = 'new year*x-mas*happy'
print(event.split('*'))
print(event.split('*')[1].split('-'))

py = 'hello*python*'
print(py.split('*',1))
print(py.split('*',2))

# A.strip(B) : 문자열 A 앞뒤의 문자열 B를 제거 / B가 없으면 공백문자 제거
# rstrip(char),lstrip(char) 도 있음
name='jimin jella ****'
print(name.strip('****'))

## 현재파일에 사용된 모든 단어를 알파벳 순으로 출력, 각 단어가 등장한 횟수 출력

strip = string.whitespace + string.punctuation + string.digits + "\"'"
print(string.punctuation)
print(string.digits)

import string
import sys
def count_unique_word():
    words={}
    strip = string.whitespace + string.punctuation + string.digits + "\"'"

    for filename in sys.argv[0:]:
        with open(filename) as file:
            for line in file:
                for word in line.lower().split():
                    word = word.strip(strip)
                    if len(word) > 2: # 2번 이상 나옴
                        words[word] = words.get(word,0) + 1

    for word in sorted(words):
        print('{}: {}번'.format(word, words[word]))

count_unique_word()


## A.swapcase() : 문자열 A에서 대소문자를 반전한 문자열의 복사본 반환
# capitalize() :  문자열 첫 글자를 대문자로 / lower() :  전체 문자열을 소문자로 /  upper() : 전체 문자열을 대문자로
hi = 'Hello hI'
print(hi.swapcase())


# A.index(sub,start,end) : 문자열 A에서 부분 문자열 sub의 인덱스 위치 반환 [실패할 경우 ValueError 예외 발생]
# A.find(sub,start,end) : 문자열 A에서 부분 문자열 sub의 인덱스 위치 반환 [실패할 경우 -1 반환]
# start, end 문자열 범위 - 생략시 전체 문자열에서 부분문자열 sub 찾음
book = 'Beauty and the beast'
print(book.find('a'))
print(book.index('a'))

## A.count(sub,start,end) : 문자열 A에서 start, end 범위 내 부분 문자열 sub가 나온 횟수 반환
print(book.count('a'))

## A.replace(old, new, maxreplace): 문자열 A에서 old문자열을 new 문자열로 maxreplace 만큼 변경한 문자열의 복사본 반환
# maxreplace 지정 X :  모든 old를 new 로 반환
print(book.replace('and','&'))
hi = 'hello and hello and hello'
print(hi.replace('hello','hi',2))
