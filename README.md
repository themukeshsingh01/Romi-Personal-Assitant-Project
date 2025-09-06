# ROMI - Personal Voice Assistant

This is a small project I made in Python.  
It is a voice assistant called Romi.  
Instead of opening websites or doing tasks manually, I can give voice commands and Romi does it for me.  

---

## What Romi Can Do

- Responds when I say "Romi"  
- Opens Google, YouTube, Facebook, LinkedIn, WhatsApp  
- Plays songs from my musiclibrary.py file  
- Gets news using NewsAPI  
- Talks back using text-to-speech  

---

## Why I Made This

I made this project to practice Python.  
It also helped me understand how voice can be changed to text, how APIs return data, and how automation saves time.  

---

## Libraries Used

- speechrecognition  
- pyttsx3  
- webbrowser  
- requests  
- musiclibrary.py (my own file for songs)  

---

## How to Run

1. Clone this project  
2. Install libraries:  
   pip install speechrecognition pyttsx3 requests  
3. Add your songs inside musiclibrary.py, for example:  

   songs = {  
       "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",  
       "shapeofyou": "https://www.youtube.com/watch?v=JGwWNGJdvx8"  
   }  

4. Run the script:  
   python romi.py  

Say "Romi" and then give a command.  

---

## Future Work

- Add weather updates  
- Store commands in a file  
- Make it understand more sentences  

---

## Author

I made this project while learning Python and Data Analytics.  
