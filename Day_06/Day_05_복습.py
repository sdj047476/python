
# 1. 뉴스 기사에서 가장 긴 단어 찾기


article = """Haliburton was carried off by team-mates after suffering a hamstring strain late in the second period.

Bennedict Mathurin scored 26 points off the bench for the Pacers, who trailed 68-59 at half-time.

"We lost the best player on the team, so my role was to step up and help the team win the game," Mathurin said.

"Ty was down but it felt like the team pretty much knew what to do. Everyone had to step up. If your name gets called, be ready to play."

Haliburton, who joined the Pacers from the Sacramento Kings in 2022, averaged a team-high 24.2 points and a league-high 12.7 assists in 32 games before the meeting with the Celtics at Gainbridge Fieldhouse in Indiana.

Boston remain top of the Eastern Conference at 28-8, while fifth-placed Indiana improved to 21-15.

Memphis Grizzlies guard Ja Morant will miss the rest of the season after injuring a shoulder in practice on Saturday."""







# 2. 영화 예매 프로그램 (dict활용)

# Movie = ['Action','Romantic','Horror']
# Popcorn = ['Cheese','Caramel','popcorn']
# MovieSelect = int(input("['1.Action','2.Romantic','3.Horror']번호 입력:"))
# PopcornSelect = int(input("['1.Cheese','2.Caramel','3.popcorn']번호 입력:"))
# MoviePrice = ['10000','8000','9000']
# PopcornPrice = ['6000','5000','5000']
# print(f"영화는 {Movie[MovieSelect-1]} 고르시고 팝콘은 {Popcorn[PopcornSelect-1]} 고르셨으므로 가격은 {MoviePrice[MovieSelect-1] + PopcornPrice[PopcornSelect-1]}원 입니다.")




# cgv = {
#     'movie':{
#         'movieList':['1.Action','2.Romantic','3.Horror'],
#         'moviePrice':[10000,8000,9000]
#     },
#     'popcorn':{
#         'popcornList':['1.Cheese','2.Caramel','3.popcorn'],
#         'popcornPrice':[6000,5000,5000]
#     }
# }
# movieChoice = int(input(f"영화를 고르세요 {cgv['movie']['movieList']}: ")) - 1
# popcornChoice = int(input(f"팝콘을 고르세요 {cgv['popcorn']['popcornList']}: ")) - 1
#
# print(f"선택한 영화: {cgv['movie']['movieList'][movieChoice]}, 선택한 팝콘: {cgv['popcorn']['popcornList'][popcornChoice]}, 가격: {cgv['movie']['moviePrice'][movieChoice] + cgv['popcorn']['popcornPrice'][popcornChoice]}원")

