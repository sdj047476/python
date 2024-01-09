
#1. 일본여행 계획 프로그램

# J = input("일본여행 계획 : 00,00,00 : ")
# JList = J.split(',')
# print(JList)

#2. 뉴스 기사 단어 찾기 프로그램

# article = """The US aviation regulator has said 171 Boeing 737 Max 9 planes will remain grounded until it is satisfied the planes are safe.
#
# The Federal Aviation Administration (FAA) has been inspecting the jets after part of an Alaska Airlines plane's fuselage fell off on Friday.
#
# The FAA said its first priority was "keeping the flying public safe".
#
# Boeing's CEO Dave Calhoun told staff that its response "is and must be" the focus of the company.
#
# Thousands of passengers saw their flights cancelled after major US airlines grounded dozens of the jets.
#
# "We have grounded the affected airplanes, and they will remain grounded until the FAA is satisfied that they are safe," the FAA said in a statement on Sunday.
#
# Boeing also said that it will hold an all-employee meeting about safety on Tuesday to address its response to the incident.
#
# "When serious accidents like this occur, it is critical for us to work transparently with our customers and regulators to understand and address the causes of the event, and to ensure they don't happen again," Mr Calhoun said.
#
# Disruptions have primarily affected flights in the US.
#
# The vast majority of Boeing 737 Max 9s used in the US are operated by United Airlines and Alaska, while Turkish Airlines, Panama's Copa Airlines and Aeromexico have also grounded jets of the same model for inspections.
#
# Alaska grounded 65 planes, and said on Sunday that it had cancelled 163 flights, or 21%. Around 25,000 people were affected. The airline said travel disruptions from the grounding of some of its planes is expected to last until at least mid-week.United has grounded 79 planes, and said on Sunday it had cancelled about 180 flights.
#
# Meanwhile, authorities are still searching for the plug door - which they believe fell to the ground in the western suburbs of Portland - and have appealed to the public to help find the panel.
#
# During Friday's incident, Alaska Airlines flight 1282 from Portland, Oregon, to Ontario, California, reached 16,000ft (4,876m) when it began an emergency descent, according to flight tracking data.
#
# Passengers on board said a large section of the plane's outer shell fell to the ground shortly after take-off."""
#
# Word = input("당신이 찾고 싶은 단어 : ")
# print(f"{article.count(Word)}")

#3. 스타벅스 메뉴 선택 프로그램

# StarCoffee = ['1.아메리카노:4000','2.라떼:5000','3.바닐라라떼:5500']
# StarCake = ['1.치즈케익:5000','2.딸기케익:6000','3.우유케익:5500']
# CoffeeP = ['4000','5000','5500']
# CakeP = ['4000','5000','5500']
# print(StarCoffee)
# print(StarCake)
# ChoiceStarCoffee = int(input("커피 번호 : "))
# ChoiceStarCake = int(input("케익 번호 : "))
# print(f"가격은 {int(CoffeeP[ChoiceStarCoffee-1]) + int(CakeP[ChoiceStarCake-1])}원 입니다.")



#4. 좋아하는 커피 브랜드 capitalize화 프로그램

brands = input("좋아하는 커피 브랜드 입력 00,00,00 : ").split(',')
brands[0] = brands[0].capitalize()
brands[1] = brands[1].capitalize()
brands[2] = brands[2].capitalize()
print(brands)



