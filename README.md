為了完成這個小專案<br>
需要將他拆解成幾個小步驟<br>
步驟如下：<br>
1.將一個影片檔轉換成wav或mp3<br>
<br>
目前想法是利用MoviePy將影片的音訊節取出來<br>
安裝moviepy只需要pip install moviepy便可<br>
<br>
參考資料：<br>
https://hardliver.blogspot.com/2017/07/moviepy-moviepy.html<br>
http://zulko.github.io/moviepy/getting_started/audioclips.html<br>
https://zulko.github.io/moviepy/getting_started/audioclips.html<br>
https://zulko.github.io/moviepy/getting_started/audioclips.html#creating-a-new-audio-clip<br>
<br>
參考寫法:<br>
from moviepy.editor import *<br>
videoclip = VideoFileClip("test.mp4")<br>
audioclip = videoclip.audio<br>
audioclip.write_audiofile("test.wav")<br>
<br>
2.將音訊檔利用SpeechRecogniton將聲音轉文字<br>
<br>
安裝speechrecognition只需pip install SpeechRecognition便可<br>
<br>
參考資料：<br>
https://ithelp.ithome.com.tw/articles/10195763<br>
https://www.youtube.com/watch?v=31DZfkYRvI4<br>
https://www.youtube.com/watch?v=3LLksqP2aXE<br>
https://ithelp.ithome.com.tw/articles/10195970<br>
https://pypi.org/project/SpeechRecognition/<br>
https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py<br>
https://cloud.google.com/speech-to-text/<br>
http://www.chiehfuchan.com/%E7%B0%A1%E5%96%AE%E5%88%A9%E7%94%A8-python-%E5%A5%97%E4%BB%B6-speechrecognition-%E9%80%B2%E8%A1%8C%E8%AA%9E%E9%9F%B3%E8%BE%A8%E8%AD%98/<br>
https://cloud.google.com/speech-to-text/docs/reference/libraries<br>
<br>
參考寫法:<br>
<br>
import speech_recognition as sr<br>
<br>
#在與此腳本相同的文件夾中獲取“english.wav”的路徑<br>
from os import path<br>
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")<br>
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")<br>
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")<br>
<br>
#使用音頻文件作為音頻源<br>
r = sr.Recognizer()<br>
with sr.AudioFile(AUDIO_FILE) as source:<br>
    audio = r.record(source)  # read the entire audio file<br>
<br>
#使用Google語音識別識別語音<br>
try:<br>
    #出於測試目的，我們只使用默認的API密鑰<br>
    #要使用其他API密鑰，請使用`r.recognize_google（audio，key =“GOOGLE_SPEECH_RECOGNITION_API_KEY”）`<br>
    # 而不是`r.recognize_google（audio）`<br>
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))<br>
except sr.UnknownValueError:<br>
    print("Google Speech Recognition could not understand audio")<br>
except sr.RequestError as e:<br>
    print("Could not request results from Google Speech Recognition service; {0}".format(e))<br>
<br>
#使用Google Cloud Speech識別語音<br>
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""<br>
try:<br>
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))<br>
except sr.UnknownValueError:<br>
    print("Google Cloud Speech could not understand audio")<br>
except sr.RequestError as e:<br>
    print("Could not request results from Google Cloud Speech service; {0}".format(e))<br>
<br>
<br><br>
========20190201========<br>
發現…用google_cloud只是協助辨識30秒內的音訊…如果要辨識30分鐘以上的音訊無法使用以上程式<br>
重新參考資料：<br>
https://cloud.google.com/speech-to-text/docs/async-recognize#speech-async-recognize-gcs-python<br>
https://cloud.google.com/speech-to-text/docs/video-model<br>
搭建python開發環境<br>
https://cloud.google.com/speech-to-text/docs/reference/libraries<br>
pip install --upgrade google-cloud-speech<br>
使用後發現只能上傳10MB的音訊檔<br>
重新找尋相關資源後，決定使用IBM Speed to Text<br>
參考資料：<br>
https://www.ibm.com/watson/services/speech-to-text/



<br>
3.將生成的文字檔讀入<br>
<br>
參考資料：<br>
<br>
參考寫法：<br>
<br>
4.進行分析，產生每個文字的正負情緒值<br>
<br>
參考資料：<br>

參考寫法：<br>
<br>
5.產生標籤雲<br>
<br>
參考資料：<br>
<br>
參考寫法：<br>
<br>
<br>
6.解析每個家人和小數點及阿比互動的頻率及正負語言出現的機率<br>
<br>
<br>
參考資料：<br>
<br>
<br>
參考寫法：<br>
<br>
<br>
<br>
最後的整合：<br>

