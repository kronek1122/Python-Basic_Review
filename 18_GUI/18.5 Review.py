import tkinter as tk

window = tk.Tk()

#Exercise 2
button = tk.Button(
    text="Click here",
    bg='white',
    fg='blue',
    width=50,
    height=25,
    )
button.pack()
window.mainloop()

#Exercise 3
entry = tk.Entry(width=40)
entry.insert(0,'What is your name?')
entry.pack()
window.mainloop()

