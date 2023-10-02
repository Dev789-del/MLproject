#Import necessary modules
import pandas as pds
import numpy as nump
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from tkinter import *
from tkinter import filedialog

#Read the data and specify data training and test
dataset_program = pds.read_csv('base_language_set.csv')
x = nump.array(dataset_program["Text"])
y = nump.array(dataset_program["language"])

cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =   0.33, random_state = 40)

#Define and activate the model
detect_model = MultinomialNB()
detect_model.fit(X_train, y_train)
detect_model.score(X_test, y_test)

#Define app main
main_app = Tk()
main_app.title("Language Detector")
main_app.geometry("600x600")

#Define detector function with method direct text 
def language_detect():
    #Create condition to input text
    if app_text.compare("end-1c", "==", "1.0" ):
        listbox.delete(0, END)
        listbox.insert(END, "You forgot to input anything...")
    else:
        # predict the language and send back result
        listbox.delete(0,END)
        input_data = cv.transform([app_text.get(1.0, END)]).toarray()
        detect_output = detect_model.predict(input_data)
        listbox.insert(END, f"Language found: {detect_output}")

#Define detector function with method select a text file
def check_language():
    # ask the clients to choose a file
    loca_file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    # read the file content
    with open(loca_file_name, 'r') as f:
        content = f.read()
        # check if the file is empty
        if not content.strip():
            listbox.delete(END, 0)
            listbox.insert(END, "You forgot to input anything...")
        else:
            # predict the language and send back result
            
            listbox.delete(0,END)
            input_data = cv.transform([content]).toarray()
            detect_output = detect_model.predict(input_data)
            listbox.insert(END, f"Language found: {detect_output}")

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

app_button = Label(main_app, text = "Output result:")
app_button.pack(pady = 10)

listbox = Listbox(main_app, width = 40, height = 5)
listbox.pack()
#Run code
main_app.mainloop()

