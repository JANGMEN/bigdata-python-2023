# 제어문
# 파이썬은 들여쓰기로 제어문, 함수의 구역에 들어있는지를 판별

money = True
if (money == True): # 제어문, 함수의 시작
    print('택시를 탑니다')
elif(money == False): # java의 else if()
    print('걸어갑니다')
else :
    print('나도 몰라')
print('여기 내립니다') # 탭이 중요!!

print(3 in [1, 2, 4, 5, 6, 7]) # 리스트 안에 3이 있는가?

while(money == False):
    print('와!!! 부럽다~')

# java의 for(int i = 0; i < 10; i++)
for i in range(0, 10):
    print(i)
l1 = [1, 3, 5, 7, 9]
for i in l1:
    print(i)

print('홀수만 찍기')
for j in range(1, 10, 2):
    print(j)

print('구구단')
for x in range(2, 10): # 2 ~ 9
    for y in range(1, 10): # 1 ~ 9
        print(f'{x} X {y} = {x * y:2d}', end=' ') #2d : 2줄로 만들어줌
    print('')

# 연습문제
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += 1
        print(i, end=', ')
    i += 1
print(result)

for i in range(1, 6):
    print('*' * i)