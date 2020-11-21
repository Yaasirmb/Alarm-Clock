from datetime import datetime
import time
from playsound import playsound

#Program that will act as an alarm clock.
print("Please enter your time in the following format: '07:30:PM \n")
def alarm (user = input("When would you like your alarm to ring? ")):
    
    when_to_ring = datetime.strptime(user, '%I:%M:%p').time()

    while True:
        time.sleep(2)

        current_time = datetime.now().time().strftime("%I:%M:%p")
        
        if when_to_ring.strftime("%I:%M:%p") == current_time:
            playsound('wake_up.mp3')

        
        print('Current time ' + current_time)

alarm()