ROMI – My Personal Voice Assistant

This is a small project I made in Python where I built my own voice assistant called Romi. The idea was simple: I wanted to stop doing repetitive tasks like opening Google, YouTube, or Facebook manually and instead just tell my computer what to do.

What Romi Can Do

Responds when I say “Romi”

Opens websites like Google, YouTube, LinkedIn, Facebook, WhatsApp

Plays songs from my own music library file

Reads out the latest news (using the News API)

Talks back to me using text-to-speech




Why I Built This

I wanted to learn how speech recognition, text-to-speech, and APIs work together in Python. Instead of making a simple “Hello World” project, I decided to make something that I could actually use. Now I can tell Romi things like:

“Open Google”

“Play believer”

“News”

And it does the task for me.




How to Run

Clone the repo

Install dependencies:

pip install speechrecognition pyttsx3 requests


(Optional) Edit musiclibrary.py with your favorite songs (YouTube links work).

Run:

python romi.py

Things I Want to Add Later

Weather updates

Better wake word detection

Maybe integration with Spotify or YouTube Music

Note

This project is still very much in progress. I mostly use it for fun and to explore how assistants like Alexa or Siri might work behind the scenes.
