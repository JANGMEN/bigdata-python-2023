# CSV 파일 읽기
import csv

# \ufeff가 숨어있을 경우 encoding='utf-8-sig'로 변경
csvfile = '충청북도_푸드뱅크현황.csv' #'부산광역시_시내버스_이용건수.csv'
dirname = './Day03/'

fr = open(f'{dirname}{csvfile}', mode='rt', encoding='utf-8-sig') # 한국어는 기본이 c(code)p(page)949
reader = csv.reader(fr, delimiter=',') #  구분자가 ,일 경우

for line in reader:
    print(line)

fr.close()