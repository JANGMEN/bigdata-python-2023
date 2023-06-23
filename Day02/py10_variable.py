# 변수에 대하여
a = 1
b = 'python'
c = [1, 2, 3]

print(id(a)) # id는 주소값
print(id(b))
print(id(c))
# 문자열은 할당, copy 동일 / 리스트 할당, copy가 다름
a = b
print(id(a))
print(id(b))
print(a is b)

from copy import copy
a = copy(b)
print(id(a))
print(id(b))
print(a is b)
