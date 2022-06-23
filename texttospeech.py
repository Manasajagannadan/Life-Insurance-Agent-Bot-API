import pyttsx3
def speech11(inp):
   engine = pyttsx3.init()
   k=''
   k=inp
   engine.say(k)
   engine.setProperty('rate',45)
   engine.setProperty('volume', 5)
   engine.runAndWait()
