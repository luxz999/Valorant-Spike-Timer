import tkinter as tkr
from PIL import ImageGrab
import keyboard

root = tkr.Tk()
root.geometry("+0+0")
root.overrideredirect(True)
root.config(bg="black")
root.attributes("-transparentcolor", "black")
root.wm_attributes("-disabled", True)
root.wm_attributes("-topmost", True)
root.resizable(0, 0)

timer_display = tkr.Label(root, font=('Trebuchet MS', 30, 'bold'), bg='black')
timer_display.pack()

seconds = 45
running = True

print("^|================ Valorant Bomb Timer ================^|")
print("^|       Train your timing skills—Not a hack!          ^|")
print("^|    Auto-detects bomb plant for better practice.     ^|")
print("^|=====================================================^|")

def cancel_timer():
    global running
    running = False
    root.wm_attributes('-alpha', 0.01)
    print("Timer Canceled!")

keyboard.add_hotkey("F8", cancel_timer) 

def countdown(time):
    global running
    if time > 0 and running:
        mins, secs = divmod(time, 60)
        def color_change(t_time):
            if t_time > 10:
                return 'green'
            elif 8 <= t_time <= 10:
                return 'yellow'
            elif t_time < 7:
                return 'red'
        timer_display.config(text="{:02d}:{:02d}".format(mins, secs), fg=color_change(time))
        root.after(1000, countdown, time - 1)
    else:
        if running:
            root.wm_attributes('-alpha', 0.01)
            search_color()

def start_countdown():
    global running
    running = True
    root.wm_attributes('-alpha', 0.7)
    countdown(seconds)

def search_color():
    area = (931, 26, 973, 66)
    screenshot = ImageGrab.grab(bbox=area)

    for x in range(screenshot.width):
        for y in range(screenshot.height):
            pixel = screenshot.getpixel((x, y))
            if pixel == (230, 0, 0) or pixel == (170, 0, 0):
                print("Detected bomb plant!")
                start_countdown()
                return
    root.after(10, search_color)

root.after(10, search_color)
root.mainloop()
