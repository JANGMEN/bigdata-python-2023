# 함수
'''
private int getMethods(int x, Object y) {
    //
    return result;
}
'''
# 함수선언 : def 함수명(파라미터) [-> 옵션]:
def add(x, y) -> any: # any : 뭐든지 다 받아서 출력하겠다
    result = x + y
    return result

def minus(x, y):
    return x - y

print(add(3, 5))
print(minus(6, 2))
print(add('Hello ', 'World')) # 입력 파라미터에 제약이 없음

def plus(x, y) -> None: # 리턴에 대한 옵션값 : None, void
    print(x + y)

plus(3, 5.4)

print(None) # NULL, null

def add_many(*args):
    result = 0
    for i in args:
        result += i
    
    return result

print(add_many(1, 2, 3))
print(add_many(3, 6, 9, 12, 15, 18, 21, 24, 27))
print(add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(add_many('Life', 'is', "strange"))

# add, minus, mult, div 한꺼번에 처리
def all_calc(x, y):
    return (x+y, x-y, x*y, x/y)

print(all_calc(601, 45))
# 함수는 무조건 하나의 값만 리턴
# 리턴값을 튜플로 처리하면 리턴을 한꺼번에 여러 개 할 수 있음
(res_add, res_min, res_mul, res_div) = all_calc(601, 45)

# 함수 기본값
def introduce_myself(name, age, man = True) -> None:
    print(f'나의 이름은 {name} 입니다')
    print(f'나이는 {age}세 입니다')
    if man:
        print(f'나는 남자입니다')
    else:
        print('나는 여자입니다')

introduce_myself('유숙', 45, False)
introduce_myself(man=False, name='애슐리', age=40) # 파라미터명 지정하면 순서에 상관없음

# 같은 이름의 변수를 사용하는 것은 지양

val = 1 # 전역변수(전체에서 쓰이는 val)

def valtest(val): # 지역변수
    val += 1
    return val

def valtest2():
    global val # 전역변수 val을 내가 함수 내에서 잠시 가져다 쓴다는 뜻
    val += 10

# def valtest2(tmp):
#     tmp += 1
#     return tmp

valtest2()
print(val)
#valtest(val)
#print(val)


# lambda

# javascript jQuery
# 익명함수
# $(document).ready = function() {
# }

# 자바스크립트 람다함수
# $(document).ready = () => {
# }

# var adds = () => { return a + b; }
adds = lambda a, b: a + b
# 위의 식과 동일
def adds(a, b):
    return a + b

print(adds(6, 7))

print(abs(-3)) # 절대값
print(all([1, 2, 4, 5])) # 반복문 없이 참, 거짓 확인하기

for i  in [1, 3, 5, 7, 0]:
    print(i)
t1 = (1, 2)