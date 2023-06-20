# 입출력

import datetime # 날짜를 모듈 가져옴

birth_year = 1994 # int(input('출생년도를 입력하세요 > ')) # 키보드 입력(키보드 입력 받은 건 무조건 String)

print(f'당신의 출생년도는 {birth_year}년 입니다.') # 콘솔 출력

current_year = datetime.datetime.now().year # now까지만 하면 yyyy-MM-dd hh:mm:ss.ms까지 다 나옴
# print(current_year)
age = current_year - birth_year
print(f'당신의 나이는 {age}세 입니다.')

a = 123
a = [3, 6, 9]
print(a)

print('Life' 'is' 'strange')
print('Life' + 'is' + 'strange') # 위의 결과와 동일
print('Life' , 'is' , 'strange') # 일반적
print('Life', 3.141592, True)

print(range(10))
print(len(range(10)))

for i in range(10):
    if i == (len(range(20)) -1):
        print(i, end='\n') # 엔터를 없앨 때
    else:
        print(i, end=', ')

print('Life', 'is', 'strance', sep='&') # 별로 안 쓰임

pi = 3.14159265359
print(f'PI = {pi:.4f}') # format string
print(f'PI = {pi:10.2f}') # format string