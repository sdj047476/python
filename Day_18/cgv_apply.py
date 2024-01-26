# cgv_apply - 3
# apply: 새로운 열을 만들기
import pandas as pd
df = pd.read_csv('cgv.csv')

def recommendPopcornForSenior(row):
    if row['ages'] == 50 and row['snacks'] == '일반 팝콘':
        return '할인 대상'
    else:
        return '할인 없음'

# 시간대 조조. 체크카드 사용. 조조 이벤트 해당됨/해당안됨
def MorningCheckCardEvent(row):
    if row['times'] == '조조' and row['payments'] == '체크 카드':
        return '조조 이벤트 해당됨'
    else:
        return '조조 이벤트 해당 안됨'

def ComboEvent(row):
    if row['snacks'] == '일반 팝콘' and row['drinks'] == '제로 콜라':
        return '제로콤보 세트'
    else:
        return '해당 없음'

df['50대 할인 이벤트'] = df.apply(recommendPopcornForSenior, axis=1)
df['조조 시간대 체크카드 이벤트'] = df.apply(MorningCheckCardEvent, axis=1)
df['제로 이벤트'] = df.apply(ComboEvent, axis=1)
print(df)
