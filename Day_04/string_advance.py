
# 내장 함수[int(),str(),float(),bool(),list(),print(),input()]
# len() : 길이를 알려주는 기능

# coffee = "americano"
# print(len(coffee)) #9
# print(coffee.upper()) #AMERICANO
# print(coffee.lower()) #americano
# print(coffee.capitalize()) #Americano
# print(coffee.strip()) #빈공간 americano 빈공간 [반공간 없애기]
# print(coffee.find('c')) #몇번째에 'c'가 있니? 5 #없으면 -1
# print(coffee.replace('cano','can')) # 왼쪽에서 오른쪽으로 바꾸기 #american
# print(coffee.count('a')) #'a'몇개니> #없으면 -1

#1. 대소문자 변환 프로그램. 사용자로부터 소문자로 된 문자열을 입력받은 후, 이를 모두 대문자로 변환하는 프로그램을 만드세요.
# Word = input("소문자로 된 문자열 입력:")
# print(f"대문자로 변환하면 {Word.upper()}")

#2. 노래 가사에서 단어 카운트. Charlie Puth의 노래 "Left And Right"에서 "left"와 "right"라는 단어가 각각 몇 번 나오는지를 세는 프로그램을 만드세요.
# 대소문자 구분 없이 카운트하세요.
# CharliePuthSong = """Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Ever since the d-day y-you went away (no, I don't know how)
# How to erase your body from out my brain (what you gon' do now?)
# Maybe I should just focus on me instead (but all I think about)
# Are the nights we were tangled up in your bed
# Oh no (oh no)
# Oh no (oh no)
# You're goin' 'round in circles
# Got you stuck up in my head, yeah
# Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind
# Your love stays with me day and night
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Ever since the d-day y-you went away (someone tell me how)
# How much more do I gotta drink for the pain (what you gon' do now?)
# You did things to me that I just can't forget (now all I think about)
# Are the nights we were tangled up in your bed
# Oh no (oh no)
# Oh no (oh no)
# You're going 'round in circles
# Got you stuck up in my head, yeah
# Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (of my mind)
# Your love stays with me day and night
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Did you know you're the one that got away?
# And even now, baby, I'm still not okay
# Did you know that my dreams, they're all the same
# Every time I close my eyes?
# Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Your love stays with me day and night
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# (Whoa)
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)"""
# LowerSong = CharliePuthSong.lower()
# print(f"가사에서 left는 {LowerSong.count('left')}개, right는 {LowerSong.count('right')}개.")
# print(f"가사의 길이는 {len(LowerSong)}")
#
#
# a = "mega"
# b = "study"
# c = a + b # + 문자열 연결 연산자 결과:megastudy
# d = a * 3 # * 문자열 반복 연산자 결과:megamegamega
# e = a[0] # [] 문자열 인덱싱 결과:m
# f = b[0:3] # [start:end] 문자열 슬라이싱(end제외) 결과:stu
# g = 'g' in a # "mega"에서 'g'가 있니? 결과:Ture or False
#
# #split 함수
# title = "megastudy python programming"
# print(title.split()) #str에서 list만들어주기
# title1 = "orange,apple,banana"
# print(title1.split(','))
#
# #user한테 이메일주소를 입력받고, ['유저아이디','도메인'] 프로그램
# # ex) python@megastudy.com ['python','megastudy.com']
#
# Emailaddress = input("이메일 주소:") #python@megastudy.com
# A = Emailaddress.split("@") #['python',;megastudy.com']
# B = A[1].split('.') #['megastudy','com']
# A[1] = B[0] #['python','megastudy']
# #A[2] = B[1] -> A[2]가 없으므로 안된다.
# A.append(B[1])
# print(A)

#join 함수
# word = ' '.join(['ice','cream']) #'ice cream'
#
# id = input("아이디 입력:") #mega
# domain = input("도메인 입력:") #naver.com
# print('@'.join([id,domain])) #mega@naver.com

#1.기사의 after를 모두 befor로 바꾸기
article = """The US aviation regulator has said 171 Boeing 737 Max 9 planes will remain grounded until it is satisfied the planes are safe.

The Federal Aviation Administration (FAA) has been inspecting the jets after part of an Alaska Airlines plane's fuselage fell off on Friday.

The FAA said its first priority was "keeping the flying public safe".

Boeing's CEO Dave Calhoun told staff that its response "is and must be" the focus of the company.

Thousands of passengers saw their flights cancelled after major US airlines grounded dozens of the jets.

"We have grounded the affected airplanes, and they will remain grounded until the FAA is satisfied that they are safe," the FAA said in a statement on Sunday.

Boeing also said that it will hold an all-employee meeting about safety on Tuesday to address its response to the incident.

"When serious accidents like this occur, it is critical for us to work transparently with our customers and regulators to understand and address the causes of the event, and to ensure they don't happen again," Mr Calhoun said.

Disruptions have primarily affected flights in the US.

The vast majority of Boeing 737 Max 9s used in the US are operated by United Airlines and Alaska, while Turkish Airlines, Panama's Copa Airlines and Aeromexico have also grounded jets of the same model for inspections.

Alaska grounded 65 planes, and said on Sunday that it had cancelled 163 flights, or 21%. Around 25,000 people were affected. The airline said travel disruptions from the grounding of some of its planes is expected to last until at least mid-week.United has grounded 79 planes, and said on Sunday it had cancelled about 180 flights.

Meanwhile, authorities are still searching for the plug door - which they believe fell to the ground in the western suburbs of Portland - and have appealed to the public to help find the panel.

During Friday's incident, Alaska Airlines flight 1282 from Portland, Oregon, to Ontario, California, reached 16,000ft (4,876m) when it began an emergency descent, according to flight tracking data.

Passengers on board said a large section of the plane's outer shell fell to the ground shortly after take-off."""

newArticle = article.replace('after','❤️').replace('it','😊').split()
print(newArticle)
