# 모듈 사용
#import datetime as dt
from datetime import datetime # as dt # 필요한 것만 가져옴
from os import getcwd

curr_date = datetime.now() #dt.datetime.now()
print(curr_date)

print(getcwd())