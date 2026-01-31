import tkinter as tk

class App(tk.Tk):
    def __init__(self, wtitle):
        super().__init__()

        self.title(wtitle)

        self.frm = tk.Frame(self)
        self.frm.grid(row= 0, column=0, padx=60, pady=30)
        
        self.entrybox = tk.Entry(self.frm)
        self.entrybox.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("~a StringVar~")

        # Tell the entry widget to watch this variable.
        self.entrybox["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrybox.bind('<Key-Return>',
                             self.print_contents)
        
        # Define callbacks for when the user enter or leave mouse in the entry.
        self.entrybox.bind("<Enter>", self.turn_red)
        self.entrybox.bind("<Leave>", self.turn_blue)
        self.entrybox.bind("<Button-1>", self.sayDone)
    
    def turn_red(self, event):
        event.widget["foreground"] = "red"        
    def turn_blue(self, event):
        event.widget["foreground"] = "blue"        
    def sayDone(self, event):
        self.contents.set("Done")        
        
    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get(), self.entrybox.get(), event.widget.get())
def main():
    App("My Do-Nothing Application").mainloop()
    
main()
