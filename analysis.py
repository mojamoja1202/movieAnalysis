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
#google Speech Recognition API key:AIzaSyBl4As7kha9o244lyKCYYjJ9zRArnaZtbM

r=sr.Recognizer()

with sr.AudioFile("tmp.wav") as source:
	audio = r.record(source) # read the entire audio file

r.recognize_google(audio,key="AIzaSyBl4As7kha9o244lyKCYYjJ9zRArnaZtbM")
