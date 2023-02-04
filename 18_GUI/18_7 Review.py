import tkinter as tk
import random


# Exercise 1
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'indigo', 'violet']

def color_change():
    btn_click['bg'] = f'{random.choice(colors)}'

window = tk.Tk()

btn_click = tk.Button(
    text = 'Click me',
    command=color_change,
)
btn_click.pack(fill=tk.BOTH)

window.mainloop()

# Exercise 2

def roll():
    lbl_value['text'] = f'{random.choice(range(1,7))}'

window= tk.Tk()

lbl_value = tk.Label(text = "Null")
lbl_value.pack(fill = tk.BOTH)

btn_roll = tk.Button(text = 'Roll', command=roll)
btn_roll.pack(fill=tk.BOTH)

window.mainloop()