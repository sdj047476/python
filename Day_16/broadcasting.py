# broadcasting - 3

from gtts import gTTS

text = "차번호 19마 1234 차주님 제발 카운터로 와주세요"
tts = gTTS(text, lang='ko')
tts.save('result.mp3')
