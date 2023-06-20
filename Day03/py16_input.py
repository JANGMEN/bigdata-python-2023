# 입력
# x, y = input('두 개 수를 입력하세요(구분자 ,) > ').split(',')

# print(type(x))
# print(type(y))

# 다중 입력
x, y = map(int, input('두 개 수를 입력하세요(구분자 ,) > ').split(','))
print(x + y)

# 출력할 때
# Escape char \n \t \b \' \" \\ == java
# formatting %d %f %s ... == java