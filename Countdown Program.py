import time
print("Welcome to the Countdown prgram")


hours = int(input("Enter how many hours :  "))
minutes = int(input("Enter how many minutes :  "))
seconds = int(input("Enter how many seconds :  "))

if hours >= 0 and minutes >= 0 and seconds > 0 :
    while hours >= 0 and minutes >= 0 and seconds > 0:
        seconds -= 1
        time.sleep(1)
        if seconds == 0 and minutes > 0:
            minutes -= 1
            seconds += 60
            if minutes == 0 and hours > 0:
                hours -= 1
                minutes += 60
            else:
                pass
        else:
            pass
        print(f'Your time : {hours:02d}:{minutes:02d}:{seconds:02d}')
else:
    print("Wrong data")

print(help(time))


#time_to_countdown = int(input("Enter the amount of seconds to countdown from "))
"""
if system == "S":
    time_to_countdown = int(input("Enter the amount of seconds to countdown from "))
    while time_to_countdown > 0:
        print(f'{time_to_countdown}')
        time_to_countdown -= 1
        time.sleep(0.99)
elif system == "M":
    time_to_countdown = int(input("Enter the amount of minutes to countdown from "))
    while time_to_countdown > 0:
        print(f'{time_to_countdown}')
        time_to_countdown -= 1
        time.sleep(59.9)
elif system == "H":
    time_to_countdown = float(input("Enter the amount of Hours to countdown from "))
    while time_to_countdown > 0:
        print(f'{time_to_countdown}')
        time_to_countdown -= 1
        time.sleep(3599.9)
else:
    print("Wrong data. Please choose from S/M/H ")
print("0 , Countdown complete ")
"""