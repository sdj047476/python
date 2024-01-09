#dict_type - 2
#key-value


# # key: 중복 안됨, 숫자 or 문자 타입만.
# # value: 중복 가능, 모든 타입 가능
# zodiac = {
#     1:'쥐',
#     2:'소',
#     3:'호랑이',
#     4:'토끼',
#     5:'용'
# } #dict type
# print(zodiac[4])
#
#
# mbti = {
#     'e':'외향적',
#     'i':'내향적',
#     's':'감각적',
#     'n':'직관적',
#     'f':'감성적',
#     't':'이성적',
#     'j':'계획적',
#     'p':'즉흥적'
# }
# YourMbti = input("당신의 mbti 입력: ")
# MbtiList = list(YourMbti) #['i', 'n', 'f', 'p']
# print(f"당신은 {mbti[YourMbti[0]]}이고 {mbti[YourMbti[1]]}이고 {mbti[YourMbti[2]]}이고 {mbti[YourMbti[3]]}입니다.")

instagram = {
    "신촌맛집":['싸다김밥','신촌순댓국','서브웨이'],
    "서강대맛집":{
        "서강대학식":['한식정식','오늘의치돈','육회덮밥']
    }
}
print(instagram["신촌맛집"][2])
print(instagram["서강대맛집"]["서강대학식"][1])



