#Python program to check language usage from a txt file with language probability
import tkinter as tk
from langdetect import *
from tkinter import filedialog
#Define main app 
method_two_detector = tk.Tk()
method_two_detector.geometry("400x400")
method_two_detector.title("Language Detector with txt file")

#create label
app_label = tk.Label(method_two_detector, text = "Please select a file with txt extension")
app_label.pack()

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
            app_label.config(text=f"The language of the file is {language}")

#Define button
my_button = tk.Button(method_two_detector, text = "Select File", command = check_language)
my_button.pack()

#Run the main function
method_two_detector.mainloop()