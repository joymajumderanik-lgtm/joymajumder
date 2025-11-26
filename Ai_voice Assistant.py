import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# -------------------------
#   Text-To-Speech Setup
# -------------------------
engine = pyttsx3.init()
engine.setProperty("rate", 165)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# -------------------------
#   Speech Recognition
# -------------------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except:
        return ""

# -------------------------
#   Command Handler
# -------------------------
def handle(cmd):

    # Time
    if "time" in cmd:
        speak(datetime.datetime.now().strftime("%I:%M %p"))
        return

    # Date
    if "date" in cmd:
        speak(datetime.datetime.now().strftime("%A, %B %d, %Y"))
        return

    # Open websites
    if cmd.startswith("open "):
        site = cmd.replace("open ", "").strip()

        # common shortcuts
        if site == "youtube":
            webbrowser.open("https://youtube.com")
        elif site == "google":
            webbrowser.open("https://google.com")
        elif site == "facebook":
            webbrowser.open("https://facebook.com")
        else:
            webbrowser.open(f"https://{site}.com")

        speak(f"Opening {site}")
        return

    # Google search
    if cmd.startswith("search "):
        query = cmd.replace("search ", "")
        webbrowser.open("https://www.google.com/search?q=" + query)
        speak(f"Searching {query}")
        return

    # Wikipedia
    if cmd.startswith("wikipedia "):
        topic = cmd.replace("wikipedia ", "")
        try:
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        except:
            speak("Topic not found on Wikipedia.")
        return

    # Exit
    if "exit" in cmd or "stop" in cmd or "quit" in cmd:
        speak("Goodbye!")
        exit()

    # Fallback
    speak("Sorry, I didn’t understand.")

# -------------------------
#   Main Program
# -------------------------
def main():
    speak("Hello ! How Can I help You ")
    while True:
        cmd = listen()
        if cmd:
            handle(cmd)

if __name__ == "__main__":
    main()
