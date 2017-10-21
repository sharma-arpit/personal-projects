import os, sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from analyze import Analyze

positives = os.path.join(sys.path[0], "positive-words.txt")
negatives = os.path.join(sys.path[0], "negative-words.txt")
dictionary = os.path.join(sys.path[0], "large.txt")

def save():
	string = entry_1.get("1.0", "end-1c")
	savelocation = filedialog.asksaveasfilename(initialdir="/home/arpit", title="Save as", filetypes = (("text files", "*.txt"), ("python files", "*.py"), ("jpeg files", "*.jpg"), ("all files", "*.*")))
	file_object = open(savelocation, "w+")
	file_object.write(string)
	file_object.close()


def open_file():
	
	filename =  filedialog.askopenfilename(initialdir = "/home/arpit",title = "Select file",filetypes = (("text files", "*.txt"), ("jpeg files","*.jpg"),("all files","*.*")))
	f = open(filename, "r+")
	string = f.read()
	f.close()
	entry_1.insert(END, string)


def check():
	analyze = Analyze(positives, negatives, dictionary)
	string = entry_1.get("1.0", "end-1c")
	misspelled, score = analyze.analyzer(string)
	for word in misspelled:
		print(word)
	
	
root = tk.Tk()
root.geometry("500x300")
root.title("Notepad")
frame_1 = Frame(root)
frame_1.pack()
frame_2 = Frame(root)
frame_2.pack(side=BOTTOM)
entry_1 = Text(root)
entry_1.pack(expand=YES, fill=BOTH)
button_4 = Button(frame_2, text="Check", fg = "blue", command = check)
button_4.pack(side=RIGHT)
button_3 = Button(frame_2, text="Open", fg="green", command = open_file)
button_3.pack(side=RIGHT)
button_1 = Button(frame_2, text="Save", fg="red", command = save)
button_1.pack(side=LEFT)
button_2 = Button(frame_2, text="Close", fg="green", command = root.destroy)
button_2.pack(side=RIGHT)
root.mainloop()
