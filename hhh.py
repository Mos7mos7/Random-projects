import webbrowser
import time
import random


while True :          #will always run until hitting CTRL+c

    sites=random.choice(['google.com','youtube.com','facebook.com','github.com','owasp.com'])
    url=f"http://{sites}"
    webbrowser.open(url)
    seconds = random.randrange(5,45)
    time.sleep(seconds)

    # trying to mess around with someone

    #feel free to add ant websites in list above
