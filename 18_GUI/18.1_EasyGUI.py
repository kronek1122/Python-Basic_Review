import easygui as gui

# Msg box with one button
gui.msgbox(msg="Hello", title='My first message box', ok_button='Click me')

# Msg box with severals buttons, return a value of button e.g.:"Red"
gui.buttonbox(msg='What is your favorite color?',
                title = 'Choose wisely...',
                choices = ('Red', 'Yellow', 'Blue'))

# Msg box with severals buttons, button return a index of button e.g.: 1
colors = ('Red', 'Yellow', 'Blue')
gui.indexbox(msg='What is your favorite color?',
                title = 'Choose wisely...',
                choices = colors)

# Enter box collect text input from a user
gui.enterbox(msg='What is your favorite color?',
                title = 'Choose wisely...',)

# Dialog box for selecting a file to open
gui.fileopenbox(title='Select a file')

# Review Excercises: 1
gui.msgbox(msg = 'Warning!', title = 'Watch out!', ok_button = "I'll be careful")

# Review Exercises: 2
gui.enterbox(msg = 'What is your name')