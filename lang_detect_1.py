#Python program to check language from a text box method with input
from tkinter import *
from langdetect import *
from langcodes import *

main_app = Tk()
main_app.title("Language Detector")
main_app.geometry("400x400")

#Define detector function with probabilities
def language_detect():
    if app_text.compare("end-1c", "==", "1.0" ):
        app_label.config(text = "You forgot to input anything...")
    else:
        language_check = detect_langs(app_text.get(1.0, END))
        app_label.config(text = f"Identify Language is: {language_check}")

#Define box
app_top = Label(main_app, text = "Input text:", height = 5, width = 10)
app_top.pack(pady = 10)

app_text = Text(main_app, height = 10, width = 40)
app_text.pack(pady = 10)

app_button = Button(main_app, text = "Detect Language", command = language_detect)
app_button.pack(pady = 10)

app_label = Label(main_app, text = "")
app_label.pack(pady = 10)
#Run code
main_app.mainloop()

