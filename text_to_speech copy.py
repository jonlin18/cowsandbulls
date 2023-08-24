#text to speech

from gtts import gTTS 
import os

text = """
So it's gonna be forever
Or it's gonna go down in flames
You can tell me when it's over, mm
If the high was worth the pain
Got a long list of ex-lovers
They'll tell you I'm insane
'Cause you know I love the players
And you love the game
'Cause we're young, and we're reckless
We'll take this way too far
It'll leave you breathless, mm
Or with a nasty scar
Got a long list of ex-lovers
They'll tell you I'm insane
But I've got a blank space, baby
And I'll write your name
"""

language = 'zh-CN'

speech = gTTS(text = text, lang = language, slow = False)
#speech.save("taylor.mp3")

os.system("afplay ~/taylor.mp3")

#file = open("draft.txt", "r").read().replace("\n", " ") for files
#speech = gTTS(text = str(file), lang = language, slow = False)
#speech.save("voice.mp3")
#os.system("afplay ~/voice.mp3")