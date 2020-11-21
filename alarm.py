from datetime import datetime
import time

#Program that will act as an alarm clock.

print("Please enter your time in the following format: '07:30:PM \n")
user = input("When would you like your alarm to ring? ")

when_to_ring = datetime.strptime(user, '%I:%M:%p').time()


while True:
    
    time.sleep(2)
   

    current_time = datetime.now().time().strftime("%I:%M:%p")
    time_to_compare = datetime.now().time().strftime("%I:%M:%p")

    #print('Time to compare against: ' + time_to_compare)
    if when_to_ring.strftime("%I:%M:%p") == current_time:
        print("ALARM SOUND")
    
    print('Current time ' + current_time)
