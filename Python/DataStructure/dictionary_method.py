## dictionary method
# 딕셔너리 메서드의 시간 복잡도는 매우 효율적
# 복사  : O(n)
# 항목 조회: O(1)
# 항목 할당: O(1)
# 항목 삭제 :O(1)
# 멤버십 테스트 in: O(1)
# 반복 : O(n)

friend = {}
friend['name'] = 'alice'
friend['age'] = 22
print(friend)
# {'name': 'alice', 'age': 22}

friend = dict({'name':'jjanggu', 'age':5})
print(friend)
# {'name': 'jjanggu', 'age': 5}

# setdefault(key, default) : 키의 존재 여부를 모른 채 접근 할 때
# key가 존재할 경우 value를 얻음
# key 존재하지 않는 경우, 딕셔너리에 저장됨
dict_data = (('k1','v1'),('k1','v2'),('k2','v1'),('k2','v3'))
tmp_dict = {}
for k,v in dict_data:
    if k in tmp_dict:
        tmp_dict[k].append(v)
    else:
        tmp_dict[k] = [v]

print(tmp_dict)
# {'k1': ['v1', 'v2'], 'k2': ['v1', 'v3']}

tmp_dict2 = {}
for k,v in dict_data:
    tmp_dict2.setdefault(k,[]).append(v) # ** 중요 ! : 하나의 키 값에 여러개의 value

print(tmp_dict2)
# {'k1': ['v1', 'v2'], 'k2': ['v1', 'v3']}

# update
# 키가 존재하면 업데이트
# 키가 없으면 추가
fam = {'jimin':22, 'wongil':52}
fam.update({'wongil':42})
print(fam)
# {'jimin': 22, 'wongil': 42}

fam.update({'myung':51})
print(fam)
# {'jimin': 22, 'wongil': 42, 'myung': 51}

## get
# 키의 value 반환, 키가 없으면 반환 X
fam = {'jimin': 22, 'wongil': 42, 'myung': 51}
print( fam.get('jimin') ) # fam['jimin'] 같은 역할
# 22

## 읽기 전용 반복가능 객체 - items, values, keys
fam = {'jimin': 22, 'wongil': 42, 'myung': 51}
print( fam.items() )
# dict_items([('jimin', 22), ('wongil', 42), ('myung', 51)])
print( fam.keys() )
# dict_keys(['jimin', 'wongil', 'myung'])
print( fam.values() )
# dict_values([22, 42, 51])

# pop(key): key 항목을 제거하고, value 반환
fam = {'jimin': 22, 'wongil': 42, 'myung': 51}
jimin_age = fam.pop('jimin')
print(jimin_age)
# 22

# clear : 딕셔너리의 모든 항목 제거
fam.clear()
print(fam)
# {}

# 딕셔너리 정렬
fam = {'jimin': 22, 'wongil': 42, 'myung': 51}
for key in sorted(fam.keys()):
    print(key, fam[key])
# jimin 22 \n myung 51 \n wongil 42

# 카운터 딕셔너리
from collections import Counter

def counter_example():
    seq1 = [1,2,3,1,2,3,5,4,1]
    seq_counts = Counter(seq1)
    print(seq_counts)

    seq2 = [1,5,6]
    seq_counts.update(seq2)
    print(seq_counts)

    seq3 = Counter(seq2)
    print(seq3)
    print(seq_counts + seq3)


counter_example()

# Counter({1: 3, 2: 2, 3: 2, 5: 1, 4: 1})
# Counter({1: 4, 2: 2, 3: 2, 5: 2, 4: 1, 6: 1})
# Counter({1: 1, 5: 1, 6: 1})
# Counter({1: 5, 5: 3, 2: 2, 3: 2, 6: 2, 4: 1})


# 연습 문제1 /  단어 횟수 세기
from collections import Counter
word = '망고 사과 딸기 바나나 키위 사과 사과 망고 키위 메론'

word_count = Counter(word.split())
print(word_count)


dice = 5
num = [1,2,3,4,5,6]
dice_num = {}

for i in num:
    b = dice - i
    if b > 0 and b <= 6:
        t = [i, b]
        dice_num.setdefault(dice,[]).append(t)
print(dice_num)
print('\n\n')

str1 = "google"

a = set(str1)

a = Counter(a)
print(a)

b = Counter(str1)
print(b)
c = b-a
word = a-c
print(word.keys())

str1 = "hello"
str1 = str1.replace('l' , 'k')
print(str1)