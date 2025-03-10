from tkinter import *

window = Tk()
window.attributes('-fullscreen', True)
window.config(background="black")

photo = PhotoImage(file='pngwing.png')

line1 = "Inactive"
label = Label(window,
              text=line1,
              font=('Arial', 50, 'bold'),
              pady=30,
              image=photo,
              compound=TOP,
              fg="red",
              bg="black")

label.place(relx=0.5, rely=0.4, anchor='center')
def button_click():

    new_window = Tk()
    new_window.attributes('-fullscreen', True)
    time = None #can put in loop to show countdown
    line2 = 'Countdown Begins in... '
    label2 = Label(new_window,
                   text=f"{line2}{time}", #used f string to put value
                   font=('Arial', 50, 'bold'),
                   )
    label2.place(relx=0.5, rely=0.5, anchor=CENTER)


button = Button(window, text="Activate")
button.config(command=button_click)
button.config(font=('Arial', 25, 'bold'))
button.config(compound="bottom")
button.place(relx=0.5, rely=0.8, anchor='center')

def fade_text(alpha=0.0, step=0.05, fade_in=True):
    """Function to fade text color from red to black and back."""
    red_value = int(alpha * 255)  # Increasing alpha means more red
    color = f"#{red_value:02x}0000"  # RGB format: (red, 0, 0)

    label.config(fg=color)

    if fade_in:
        if alpha < 1:
            window.after(50, fade_text, alpha + step, step, True)  # Continue fading to red
        else:
            window.after(1000, fade_text, 1, step, False)  # Pause, then start fading to black
    else:
        if alpha > 0:
            window.after(50, fade_text, alpha - step, step, False)  # Continue fading to black
        else:
            window.after(1000, fade_text, 0, step, True)  # Pause, then start fading to red

# Start the fade effect
fade_text()

window.mainloop()
