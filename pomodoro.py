import time
import tkinter as tk
from tkinter import messagebox

def pomodoro_timer():
    work_duration = 25 * 60  # 25 minutes in seconds
    break_duration = 5 * 60  # 5 minutes in seconds

    start_button.config(state=tk.DISABLED)  # Disable the start button during timer

    for _ in range(2):  # Run 2 work-break cycles
        # Work session
        timer_label.config(text="Work session", fg="green")
        for _ in range(work_duration, -1, -1):
            timer_label.config(text=f"Time Remaining: {_:02d}")
            root.update()
            time.sleep(1)

        # Break session
        timer_label.config(text="Break session", fg="red")
        for _ in range(break_duration, -1, -1):
            timer_label.config(text=f"Time Remaining: {_:02d}")
            root.update()
            time.sleep(1)

    messagebox.showinfo("Pomodoro Timer", "Timer completed!")
    start_button.config(state=tk.NORMAL)  # Enable the start button after timer completes

root = tk.Tk()
root.title("Pomodoro Timer")

timer_label = tk.Label(root, text="Time Remaining:", font=("Arial", 18), fg="black")
timer_label.pack(pady=10)

start_button = tk.Button(root, text="Start", font=("Arial", 12), command=pomodoro_timer)
start_button.pack(pady=10)

root.mainloop()
