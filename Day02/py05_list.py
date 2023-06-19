# 리스트 계속
a = [1, 2, 3]
print(a)

print(a.pop()) #pop : 리스트 맨 마지막 요소를 꺼내라

print(a) # 3을 꺼냈기 때문에 1, 2만 나옴

a.append(10)
print(a)

print(a.count(2)) # count 안의 요소가 리스트 안에 몇 개 들어있는가, 요소가 없으면 0 나옴

# 리스트 확장 a = 1, 2, 10
a.extend([5, 3, 2])
print(a)

print(a.count(2))