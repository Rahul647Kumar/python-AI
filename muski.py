import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
import smtplib
import subprocess
import openai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)pip install
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Muskaan Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def play_song_by_name(song_name, music_folder):
    song_files = [f for f in os.listdir(music_folder) if os.path.isfile(os.path.join(music_folder, f))]
    for song_file in song_files:
        if song_name.lower() in song_file.lower():
            song_path = os.path.join(music_folder, song_file)
            os.startfile(song_path)
            return True
    print(f"Song '{song_name}' not found in the music folder.")
    return False

movie_process = None  # Initialize movie_process outside the function

def open_random_movie(movie_dir):
    global movie_process  # Access the global movie_process variable
    movie_files = [f for f in os.listdir(movie_dir) if os.path.isfile(os.path.join(movie_dir, f))]
    if movie_files:
        random_movie = random.choice(movie_files)
        movie_path = os.path.join(movie_dir, random_movie)
        try:
            movie_process = subprocess.Popen([movie_path], shell=True)
            print(f"Now playing: {random_movie}")
        except Exception as e:
            print(f"Error playing movie: {e}")
    else:
        print("No movie files found in the directory.")

if __name__ == "__main__":
    wishMe()

    movie_process = None

    while True:
    #if 1:
        query = takeCommand().lower()
        sites = [["youtube", "https://www.youtube.com"],["stackoverflow", "https://www.stackoverflow.com"],["google", "https://www.google.com"],["wikipedia", "https://www.wikipedia.com"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open notepad' in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        #elif 'open ms word' in query:
         #   npath =
        #    os.startfile(npath)

            # Inside your main loop, add a condition to handle the command for opening a movie.
        elif 'play movie' in query:
            movie_dir = 'C:\\Users\\Asus\\Downloads\\movies'
            open_random_movie(movie_dir)

        elif 'play song' in query:
            # Extracting the song name from the query
            song_name = query.replace('play song', '').strip()
            # Specifying the path to the music folder
            music_folder = "C:\\Users\\Asus\\Downloads\\songs"
            # Call the function to play the song by its name
            play_song_by_name(song_name, music_folder)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Sir, today's date is {strDate}")

        elif 'open vs editor' in query:
            codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'blender' in query:
            codePath = "C:\\Program Files\\Blender Foundation\\Blender 3.4\\blender-launcher.exe"
            os.startfile(codePath)
        elif 'open ps' in query:
            codePath = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe"
            os.startfile(codePath)

        elif 'open as' in query:
            codePath = "C:\\Program Files\\Adobe\\Adobe After Effects 2022\\Support Files\\AfterFX.exe"
            os.startfile(codePath)


        elif 'open pycharm' in query:
            codePath = "C:\\Users\\Asus\\OneDrive - galgotiasuniversity.edu.in\\Desktop\\PyCharm Community Edition 2023.3.4\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'open idea' in query:
            codePath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2023.3.4\\bin\\idea64.exe"
            os.startfile(codePath)

        elif 'close idea' in query:
            os.system("taskkill /F /IM idea64.exe")

        elif 'bye' in query:

            speak("Hello baby I am Sleeping bye bye.!")

            hour = int(datetime.datetime.now().hour)

            if hour >= 0 and hour < 12:

                speak("Good Morning!")


            elif hour >= 12 and hour < 18:

                speak("Good Afternoon!")


            else:

                speak("Good night!")

            bye()# This will exit the program how to exit
