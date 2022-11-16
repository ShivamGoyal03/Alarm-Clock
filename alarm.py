import tkinter as tk
import datetime
import time
import winsound
from threading import *
from PIL import Image, ImageTk

# Create Object
alarm_clock = tk.Tk()
# Set geometry
alarm_clock.minsize(400,200)
alarm_clock.maxsize(400,200)

# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        # Wait for one seconds
        time.sleep(1)
        # Get current time1
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            # winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            # winsound.Beep(23511,5)
            # winsound.PlaySound('Welcome.wav', winsound.SND_FILENAME)
            freq = 5000

            # duration is set to 100 milliseconds
            dur = 2000

            winsound.Beep(freq, dur)
            winsound.Beep(freq, dur)


# Add Labels, Frame, Button, Optionmenus
tk.Label(alarm_clock, text="Alarm Clock").pack(pady=10)
# Label(alarm_clock,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
tk.Label(alarm_clock, text="Set Time").pack()
# Label(alarm_clock,text="Set Time",font=("Helvetica 15 bold")).pack()
frame = tk.Frame(alarm_clock)
frame.pack()
hour = tk.StringVar(alarm_clock)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])
hrs = tk.OptionMenu(frame, hour, *hours)
hrs.pack(side=tk.LEFT)
minute = tk.StringVar(alarm_clock)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
mins = tk.OptionMenu(frame, minute, *minutes)
mins.pack(side=tk.LEFT)
second = tk.StringVar(alarm_clock)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
secs = tk.OptionMenu(frame, second, *seconds)
secs.pack(side=tk.LEFT)

tk.Button(alarm_clock, text="Set Alarm", command=Threading).pack(pady=20)
tk.Button(alarm_clock, text="Disable", command=alarm_clock.destroy).pack(pady=20)

# Button(alarm_clock,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)
# Execute Tkinter
alarm_clock.mainloop()
