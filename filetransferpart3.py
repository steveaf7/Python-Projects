

from tkinter import *
import tkinter as tk
import tkinter.filedialog
import shutil
import os
import time
from tkinter import messagebox

def askQuit(self):
    if messagebox.askokcancel("Exit Program", "Ok to exit application"):
        self.master.destroy()
        os._exit(0)

def askDir(self):
    global source 
    source = tk.filedialog.askdirectory() #saves the directory so we can use it later
    self.txt_browse1.insert(END,source) #prints the directory to the text box so the users can see it. 

def askDir2(self):
    global destination
    destination = tk.filedialog.askdirectory()
    self.txt_browse2.insert(END,destination)

#checks if file is older than 24 hours
def is_file_older_than_1_day(file):
    file_time = os.path.getmtime(file)
    return((time.time() - file_time)/3600>24)

def transferFiles(self):
    #creates a list of all files in the directory to be moved from.
    files = os.listdir(source)
    for file in files: #iterates through list of files
        #if files is not older than 1 day,
        if not is_file_older_than_1_day(source+'/'+file):
            # move to selected destination folder.
            shutil.move(source+'/'+file,destination)
    #deletes the files from the txt boxes
    self.txt_browse1.delete(0,END)
    self.txt_browse2.delete(0,END)
    #prints a message to the bottom text box.
    text = "Your files have been successfully transferred."
    self.txt_browse2.insert(0,text)

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        self.master = master
        self.master.title("File Transfer Program")

        #labels for above the text boxes
        self.lbl_transferFrom = Label(self.master,text="Source")
        self.lbl_transferFrom.grid(row=0,column=4,pady=(20,0))
        self.lbl_transferTo = Label(self.master,text="Destination")
        self.lbl_transferTo.grid(row=2,column=4)
        
        #left side browse buttons that open up a window to choose a file.
        self.btn_browse1 = Button(self.master,width=12,height=1,text="Browse...",command=lambda: askDir(self))
        self.btn_browse1.grid(row=1, column=0, columnspan=1, padx=20, pady=10 )
        self.btn_browse2 = Button(self.master,width=12,height=1,text="Browse...",command=lambda: askDir2(self))
        self.btn_browse2.grid(row=3, column=0, columnspan=1, padx=20, pady=10)

        #button to click to execute transfer of files newer than 24 hours 
        self.btn_check = Button(self.master,width=12,height=2,text="Transfer Files",command=lambda: transferFiles(self))
        self.btn_check.grid(row=4, column=0, columnspan=3, padx=20, pady=10 )

        #text boxes
        self.txt_browse1 = Entry(self.master,width=50)
        self.txt_browse1.grid(row=1, column=4,  padx=10, pady=10)
        self.txt_browse2 = Entry(self.master,width=50)
        self.txt_browse2.grid(row=3, column=4,  padx=10, pady=10)


        self.btn_close = Button(self.master,width=12,height=2,text="Close Program",command=lambda: askQuit(self))
        self.btn_close.grid(row=4, column=4, columnspan=3, padx=10, pady=10,sticky=E)





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
