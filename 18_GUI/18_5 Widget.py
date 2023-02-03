import tkinter as tk

#Relief styles
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)

    label = tk.Label(master=frame,text=relief_name)
    label.pack()

window.mainloop()


#Frame
frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(
    master = frame_a,
    text = 'Frame A',
    fg='blue',
    bg='white',
    width=30,
    height=5)
label_a.pack()

label_b = tk.Label(
    master = frame_b,
    text = 'Frame B',
    fg='white',
    bg='#34A2FE',
    width=30,
    height=5)
label_b.pack()

frame_b.pack()
frame_a.pack()

window.mainloop()

#Entry and button window
entry = tk.Entry(
    fg='yellow',
    bg='blue',
    width=50,
)
entry.pack()

button = tk.Button(
    text='Click me',
    width=25,
    height=1,
    bg='blue',
    fg='yellow',
)
button.pack()
window.mainloop()

#Text box window
text_box = tk.Text()
text_box.pack()
window.mainloop()


