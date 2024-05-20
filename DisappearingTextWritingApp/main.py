from tkinter import *


# Logic
user_text = ""
timer = None

# Counting method
def start_counting(event):
    global timer, user_text

    if timer is not None:
        window.after_cancel(timer)
    
    if event.keysym == "BackSpace":
        user_text = user_text[0: len(user_text)-1]
    elif event.char:
        user_text += event.char
        timer = window.after(5000, reset_app)
    
    return

def reset_app():

    global timer, user_text

    typing_area.delete('1.0', 'end')
    user_text = ""
    timer = None
    return

def save_text():
    
    global user_text

    if user_text == "":
        return
    try:
        f = open('usertext.txt', 'r')
    except FileNotFoundError:
        f = open('usertext.txt', 'w')
        f.write(user_text)
        user_text = ""
        return
    else:
        cont = f.read()
        if cont == "":
            written_text = user_text
        else:
            written_text = f'\n{user_text}'
        
        with open('usertext.txt', 'a') as f:
            f.write(written_text)
            user_text = ""
    finally:
        return


# UI
# Colors
border = 'white'
fg = 'beige'
bg = 'blue'

#font
font_size1 = 14
font_size2 = 18
font_size3 = 24

font1 = 'Calibri'
font2 = 'Helvetica'

font_style1 = 'normal'
font_style2 = 'italic'
font_style3 = 'bold'

paragraph_font1 = (font1, font_size1, font_style3)
paragraph_font2 = (font1, 12, font_style2)
head_font = (font2, font_size3, font_style1)

header = "Keep Writing or Disappear"
instruction = "if you don't press any key for 5 seconds, the text you have written will be gone"

# Create the window
window = Tk()
window.title('Disappearing Text')
window.config(bg=bg, padx=20, pady=10)

# Creating Widgets
# Create header UI
heading = Label(text=header, font=head_font, bg=bg, fg=fg, padx=10, pady=10)

# Create instruction UI
instruction_ui = Label(text=instruction, font=paragraph_font2, fg=fg, bg=bg, pady=10)

# Create typing are for users
typing_area = Text(font=paragraph_font1, bg=bg, fg=fg, width=100, height=15, wrap='w', highlightcolor=border, highlightthickness=5, highlightbackground=border, padx=5, pady=5)

typing_area.bind('<KeyPress>', start_counting)

# Reset Button
reset_button = Button(text='Reset', fg=fg, bg=bg, font=paragraph_font1, highlightbackground=bg, highlightcolor=fg, highlightthickness=1, border=3, command=reset_app, width=50)

# Save Button for save typed text as txt file
save_button = Button(text='Save', fg=fg, bg=bg, font=paragraph_font1, highlightbackground=bg, highlightcolor=fg, highlightthickness=1, border=3, command=save_text, width=50)

# Widgets placement
heading.grid(row=0, column=0, columnspan=3)
instruction_ui.grid(row=2, column=0, columnspan=3)
typing_area.grid(row=3, column=0, columnspan=3)
reset_button.grid(row=4, column=0, columnspan=2)
save_button.grid(row=4, column=2, columnspan=3)

# Start the app
window.mainloop()

