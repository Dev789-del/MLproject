#Python program to check language from a text box method with input
from tkinter import *
from langdetect import *
from langcodes import *
from tkinter import filedialog
import pycountry

#Define app main
main_app = Tk()
main_app.title("Language Detector")
main_app.geometry("700x700")

#Define detector function with probabilities
def language_detect():
    if app_text.compare("end-1c", "==", "1.0" ):
        app_label.config(text = "You forgot to input anything...")
    else:
        listbox.delete(0, END)
        language_check = detect_langs(app_text.get(1.0, END))
        for lang in language_check:
            lang_code = lang.lang
            lang_prob = round(lang.prob * 100, 3)
            name = pycountry.languages.get(alpha_2=lang_code).name
            listbox.insert(END, f"{name} -{lang_prob}%")

#Define detector function 
def check_language():
    # ask the clients to choose a file
    loca_file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    # read the file content
    with open(loca_file_name, 'r') as f:
        content = f.read()
        # check if the file is empty
        if not content.strip():
            app_label.config(text="The file is empty")
        else:
            # detect the language
            language = detect_langs(content)
            listbox.delete(0, END)
            for lang in language:
                lang_code = lang.lang
                lang_prob = round(lang.prob * 100, 3)
                name = pycountry.languages.get(alpha_2=lang_code).name
                listbox.insert(END, f"{name} -{lang_prob}%")

#Define box
method2_label = Label(main_app, text = "Please select a file with txt extension", height = 5)
my_button = Button(main_app, text = "Select File", command = check_language)

app_top = Label(main_app, text = "Input text:", height = 3)

method2_label.pack()
my_button.pack()
app_top.pack()

app_text = Text(main_app, height = 10, width = 40)
app_text.pack(pady = 10)

app_button = Button(main_app, text = "Detect Language", command = language_detect)
app_button.pack(pady = 10)

listbox = Listbox(main_app, width = 40, height = 5)
listbox.pack()
#Run code
main_app.mainloop()

