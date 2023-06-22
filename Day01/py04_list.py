# 리스트
import datetime

value = datetime.datetime.now()
lists = [1, 2, 3, 4, [5, 6, 7], True, 'Hello', value] # python은 리스트에 이렇게 넣을 수 있음

print(lists)
print(lists[-2])
print(lists[-1]) # JAVA : Null

print(lists[4][1]) # 4번째 [5, 6, 7] 중에서 [1] 이므로 6 출력
print(lists[-2][-1]) # 'Hello'에서 [-1] 이므로 o 출력

print(lists[:4]) # 파이썬 특징) 두 번째 값은 찾고 싶은 마지막 인덱스 값 + 1

# 리스트 연산
a = [1, 2, 3]
b = [4, 6, 8]
print(a + b)
print(a * 2) # a 리스트 값들에 2를 곱하는 게 아닌 2번 반복

a[2] = False # 2번 인덱스에 False를 할당
print(a)

# 리스트 함수 (문자열 함수만큼 중요)
c = [3, 6, 9]
c.append(12) # 리스트 마지막에 추가
print(c)

d = [6, 4, 9, 3, 2, 1]
d.sort() # 오름차순 정렬
print(d)

e = [3, 4, 6, 2, 5]
e.reverse() # 순서 뒤집기 (정렬 X)
print(e)

e.sort(reverse=True) # 내림차순 정렬
print(e)

e.insert(2, 5.5) # 2번 인덱스에 5.5 추가
print(e)

print(e.index(5.5)) # 값의 위치 찾기

e.append(6)
print(e)
e.remove(6) # 값 지우기 (하나만), 앞에 있던 값이 사라짐
print(e)