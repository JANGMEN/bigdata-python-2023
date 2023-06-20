# 클래스 예제
class Calculator:
    # result = 0

    def __init__(self) -> None: # self : 클래스를 선언하기 위해 사용하는 키워드
        self.result = 0 # 어디서나 사용 가능
    
    def add(self, num): # 앞에있는 self 안씀
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
    def mul(self, num):
        pass # 무슨 내용을 작성해야 할 지 모를 때 임시로 넣음

mycalc = Calculator() # java와 달리 new가 없음
print(mycalc.add(40))
print(mycalc.add(50))
print(mycalc.sub(15))

val = 10
if val != 10:
    pass