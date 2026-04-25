import os
import subprocess #this is important for the code to use facts of the system
from datetime import datetime #this is used for the jarvis to know time and date

def greet_me():
    user = os.environ.get('USER', 'Renz')
    hour = datetime.now().hour

    if hour < 12:
        greet = "Good morning, Renz"
    elif 12 <= hour < 18:
        greet = "Good afternoon, Renz"
    else:
        greet = "Good evening, Renz"
    
    print(f"--- {greet}, {user}, jarvis is online.---")
greet_me()

while True:
    #so this is the command box next to the jarvis, you can type your commands here
    query = input("Whats the next move, Renz? >> ").lower()

    if "exit" in query or "sleep" in query:
        print("System powering down, Goodbye for now, Renz.")
        break

    elif "time" in query:
        now = datetime.now().strftime("%I:%M:%S %p")
        print(f"The current time is {now}.")
    elif "browser" in query or "internet" in query:
        print("Opening your default web browser...")
        subprocess.run(["firefox"])
    elif "file" in query or "folder" in query:
        print("Opening your file explorer...")
        subprocess.run(["gio", "open", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif "youtube" in query:
        print("Opening YouTube...")
        subprocess.run(["firefox", "https://www.youtube.com"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif "roblox" in query or "Roblox" in query or "sober" in query or "Sober" in query:
        print("Opening Roblox website...")
        subprocess.run(["firefox", "https://www.roblox.com"])
    elif "nerd app" in query or "mission jeet" in query or "hell" in query:
        print("Opening Mission Jeet (or, nerd app as you say)...")
        subprocess.run(["firefox", "https://missionjeet.in/"])
    elif "shop" in query or "amazon" in query:
        print("Opening Amazon...")
        subprocess.run(["firefox", "https://www.amazon.in/"])
    elif "government" in query:
        print("Opening government website...")
        subprocess.run(["firefox", "https://www.MyGov.in/"])
    elif "idk what to say" in query or "idk what to do" in query:
        print("Just ask me to open something, Renz. I can open your browser, file explorer, and even specific websites like YouTube, Roblox, and Amazon.")
    elif "github" in query or "code" in query or "my app" in query:
        print("Opening GitHub...")
        subprocess.run(["firefox", "github.com"])
    elif "help" in query or "commands" in query or "/help" in query:
        print("Here are some commands you can try:")
        print("- 'time' to know the current time")
        print("- 'browser' or 'internet' to open your default web browser")
        print("- 'file' or 'folder' to open your file explorer")
        print("- 'youtube' to open YouTube")
        print("- 'roblox' or 'sober' to open the Roblox website")
        print("- 'nerd app' or 'mission jeet' to open the Mission Jeet website")
        print("- 'shop' or 'amazon' to open Amazon")
        print("- 'government' to open the government website")
        print("- 'weather' to open the weather forecast")
        print("- 'money eater' or 'pocket filled fatty' or 'a dumbass' to open their respective websites")
        print("- 'github' or 'code' or 'my app' to open GitHub")
        print("- I can also enable study mode automatically on week days from 4:10 PM to 6:10 PM as per due to tution")
    elif "sup dumbass" in query or "sup idiot" in query:
        print("Wsg loser, What you want now?.") #THIS IS A EASTER EGG MUHEHEHEHE
    elif "Weather" in query or "weather" in query:
        print("Opening weather forecast...")
        subprocess.run(["firefox", "https://city.imd.gov.in/citywx/responsive/?id=43295"])
    elif "money eater" in query or "pocket filled fatty" in query or "a dumbass" in query:
        print("Opening A (not so) great womans wiki...")
        subprocess.run(["firefox", "https://en.wikipedia.org/wiki/Nirmala_Sitharaman"])
    elif "github" in query or "code" in query or "my app" in query:
        print("Opening GitHub...")
        subprocess.run(["firefox", "github.com"])


from datetime import datetime
import subprocess

def auto_enforcer():
    now = datetime.now()
    day = now.strftime("%A")
    current_time = now.strftime("%H:%M")
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

if day in weekdays:
    if "16:10" <= current_time <= "18:10":
        print(f"WEEKDAY DETECTED :- {day}, TIME:- {current_time}, Initiating auto study sequence...")
    else:
        pass
    subprocess.run("pkill -f roblox", shell=True)
else:
    print(f"WEEKEND DETECTED :- {day}, TIME:- {current_time}, Enjoy your day off, Renz!")