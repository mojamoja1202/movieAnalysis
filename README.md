為了完成這個小專案<br>
需要將他拆解成幾個小步驟<br>
步驟如下：<br>
1.將一個影片檔轉換成wav或mp3<br>
<br>
目前想法是利用MoviePy將影片的音訊節取出來<br>
<br>
參考資料：<br>
https://hardliver.blogspot.com/2017/07/moviepy-moviepy.html<br>
http://zulko.github.io/moviepy/getting_started/audioclips.html<br>
<br>
參考寫法:<br>
from moviepy.editor import VideoFileClip<br>
videoclip = VideoFileClip("some_video.avi")<br>
audioclip = videoclip.audio<br>
audioclip.write_audiofile("xxxxxx.mp3")  # 如果想要輸出 mp3<br>
<br>
2.將音訊檔利用SpeechRecogniton將聲音轉文字<br>
<br>
參考資料：<br>
https://ithelp.ithome.com.tw/articles/10195763<br>
https://www.youtube.com/watch?v=31DZfkYRvI4<br>
https://www.youtube.com/watch?v=3LLksqP2aXE<br>
https://ithelp.ithome.com.tw/articles/10195970<br>
https://pypi.org/project/SpeechRecognition/<br>
https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py<br>
<br>
參考寫法:<br>
<br>
<br>
<br>
<br>
3.將生成的文字檔讀入<br>
<br>
參考資料：<br>
<br>
參考寫法：<br>
<br>
4.進行分析，文生每個文字的正負情緒值<br>
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
最後的整合：<br>
