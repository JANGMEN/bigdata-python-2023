# 딕셔너리

iron_man = {'name' : 'Tony Stark', 'address' : 'New York', 'armer' : 'Repluser Arm'}

print(iron_man)

# 아래 두 개 결과 동일
print(iron_man.get('name'))
print(iron_man['name'])

# Key 중복불가
d1 = {1 : 'a', 1: 'b'}
print(d1)

# Value 중복허용
d2 = {1 : 'test', 2: 'test'}
print(d2)

print(iron_man.keys())

for item in iron_man.keys() :
    print(item)

print(iron_man.values()) # values(), items()는 많이 사용하지 않음

print(iron_man.items())