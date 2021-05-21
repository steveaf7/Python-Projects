



from tkinter import *
import tkinter as tk
import webbrowser

def openPage(self):
    #get the text that has been typed into the entry box
    text = self.txt_body.get("1.0", END)
    #html template that adds to text to body
    html = """
    <html>
        <body>
            {}
        <body>
    <html>
    """.format(text)
    #creates a new file if not already created
    f = open("newwebsite.html",'w')
    #writes html to newly created html file, overwrites if anything in there aleady
    f.write(html)
    f.close()
    #opens the newly created page in a new tab of your browser
    webbrowser.open_new_tab("newwebsite.html")
    

class ParentWindow(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title("Web page Generator")

        #label above text input box
        self.lbl_body = tk.Label(self.master,text="Type Body for webpage here:")
        self.lbl_body.grid(row=0,column=0,padx=20,pady=10)

        #defines a text box for inputting the body of the webpage
        self.txt_body = tk.Text(self.master,width=50,height=6)
        #paints the text box to the page.
        self.txt_body.grid(row=1,column=0,padx=20,pady=10)

        #creates the button below that when clicked, will call the function openPage
        self.btn_createPage = tk.Button(self.master,width=20,height=1,text="Open Page in Browser",command=lambda: openPage(self))
        self.btn_createPage.grid(row=2,column=0,padx=20,pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
