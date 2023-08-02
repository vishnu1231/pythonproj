from gtts import gTTS
from playsound import playsound
audio = "audiofile.mp3"
language = 'en'
text=input()
speech = gTTS(text,lang=language,slow=False)
speech.save(audio)
playsound(audio)
print('sucuessfully running')