##引入所需的lib
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from os import path



#將影片讀入轉成wav or mp3
#這邊運用的是moviepy套件

videoclip=VideoFileClip('test.mp4')
audioclip=videoclip.audio
audioclip.write_audiofile("tmp.wav")

#將音訊檔轉換成文字檔
#這邊使用的套件是Speech_Recognition
#google Speech Recognition API key:xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GOOGLE_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
lang="zh-TW"
AUDIO_FILE=path.join(path.dirname(path.realpath(__file__)),"tmp.wav")
r=sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
	audio = r.record(source) # read the entire audio file

#r.recognize_google(audio,language=lang)
try:
	print("讀取結果："+r.recognize_google(audio,language=lang))
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service;{0}".format(e))
