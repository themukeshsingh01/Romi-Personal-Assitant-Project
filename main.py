import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests


r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(n):
     if   "open google" in n.lower():
          webbrowser.open("https://google.com")
     elif "open youtube" in n.lower():
          webbrowser.open("https://youtube.com")
     elif "open facebook" in n.lower():
          webbrowser.open("https://facebook.com")
     elif "open linkedin" in n.lower():
          webbrowser.open("https://linkedin.com")
     elif "open whatsapp" in n.lower():
          webbrowser.open("https://whatsapp.com")
     elif "hotstar" in n.lower():
          webbrowser.open("https://youtu.be/uSCHmIQ9mo0?si=Bqx51hTevunpWHCB")
     
     elif n.lower().startswith("play"):
          c = n.lower().split(" ")[1]
          link = musiclibrary.songs[c]
          webbrowser.open(link)
     elif "news" in n.lower():
          url = 'https://newsapi.org/v2/everything'
          params = {

               'q': 'tesla',                  # We're searching for articles that mention "tesla"
               'from': '2025-03-09',          # Only get news from this date onwards
               'sortBy': 'publishedAt',       # Sort the articles by when they were published
               'apiKey': 'e8b4c2a876724e5882fe6a837d06c7c6'  # This is your unique API key (acts like a password to use the API)

               }
          res = requests.get(url, params=params)
          for i, a in enumerate(res.json().get('articles', []), 1):
                   print(f"{i}. {a['title']}")

if __name__ == "__main__":
    speak("initialising romi.....")
    print("romi is active..")
    

while True:
        print("listening...")
        
        with sr.Microphone() as source:
             audio = r.listen(source )
        try:
            # recognize speech using Google Speech Recognition
            word = r.recognize_google(audio)

            print(word)
            if(word.lower() == "romi"):
                 speak("yes sir..")
            print("romi is now waiting for you order..")

            with sr.Microphone() as source: audio = r.listen(source)

        
            # recognize speech using Google Speech Recognition
            command = r.recognize_google(audio)
            print(command)
            processcommand(command)


        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))