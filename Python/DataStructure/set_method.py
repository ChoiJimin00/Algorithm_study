## set method

# add: 추가
fruits = {"apple","banana","orange"}
fruits.add("mango")
print(fruits)
# {'apple', 'orange', 'mango', 'banana'}


# union: 합집합 반환
fruits = {"apple","banana","orange"}
fruits = fruits.union({"kiwi","strawberry","banana"})
print(fruits)
# fruits = {"apple","banana","orange"}

# intersection: 교집합 반환
yummy = {"apple","samsung","vega"}
yummy_fruits = fruits.intersection(yummy)
print(yummy_fruits)
# {'apple'}

# difference: 차집합 반환
fruit_yummy = fruits.difference(yummy)
print(fruit_yummy)
# {'orange', 'banana', 'kiwi', 'strawberry'}

# clear: 삭제
fruits.clear()
print(fruits)
# set()

# discard: 특정 항목 제거
fruits = {'apple', 'banana', 'kiwi', 'orange', 'strawberry'}
fruits.discard('apple')
print(fruits)
# {'banana', 'orange', 'strawberry', 'kiwi'}

# remove: 특정 항목 제거 - 제거할 항목 없는 경우 KeyError
fruits.remove('kiwi')
print(fruits)
# {'banana', 'strawberry', 'orange'}

# pop: 무작위로 항목 제거 - set이 비어 있는 경우 KeyError
fruits.pop()
print(fruits)
# {'banana', 'orange'}