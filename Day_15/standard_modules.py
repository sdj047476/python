# standard_modules - 4
# random: 랜덤 역할을 하는 도구 모음
# math: 수학 관련된 도구 모음
# datetime: 날짜와 시간을 다루는 도구 모음
# os: 파일 또는 운영 체제 접근
from random import *
randint(0, 100)

from math import *
sqrt(100)

from datetime import *
now = datetime.now()
print(now) # 현재 시간

import os
p = os.path.join(os.environ['USERPROFILE'], 'DESKTOP')
folder_name = "메가스터디 커피킹"
new_p = os.path.join(p, folder_name)
os.makedirs(new_p)
