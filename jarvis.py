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