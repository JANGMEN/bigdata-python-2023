# 에러 / 예외 디버깅..

def add(x, y):
    result = 0
    result = x + y
    return result

def writeText(fname, text):
    try:
        f = open(fname, mode='w', encoding='utf-8')
        f.write('text')
        f.write('\n')
        f.close()

        print(f'{fname} 생성완료')
    except Exception as e:
        print(f'예외발생 {e}')
    finally: # 예외가 발생하든 안하든 무조건 실행되는 부분
        print('파일생성 종료!')
    # except UnboundLocalError as e:
    #     print(f'예외발생 {e}')

def divide(x, y):
    result=  0
    try:
        result = x / y
        pass
    except Exception as e:
        print(f'예외발생 {e}')
        return result

# java와 같은 프로그램 엔트리 포인트
if __name__ == '__main__':
    res = divide(7, 2)
    print(res)
    writeText(fname='예제.txt', text="랄랄라")

# 빨간 밑줄 : 문법 오류
    