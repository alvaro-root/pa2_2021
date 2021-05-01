"""
Generic shell program to illustrate GUI programming with Tkinter

This will...

Mark Foley
March 2021
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


class MyGUI:
    """
    All of the GUI stuff lives here
    """

    def __init__(self, parent):
        """
        All of the GUI 'look' lives here.
        """
        self.parent = parent

        self.parent.title("This text displays in the title bar")
        self.parent.geometry("600x600")

        # Make protocol handler to manage interaction between the application and the window handler
        self.parent.protocol("WM_DELETE_WINDOW", self.catch_destroy)

        self.padding = {'padx': 5, 'pady': 5, 'sticky': tk.W}

        self.frame1 = ttk.Frame(self.parent)
        self.frame1.grid(row=0, column=0, **self.padding)

        self.label1 = tk.Label(self.frame1, text="Label text",).grid(row=0, column=0, **self.padding)

        # set up menu
        self.menu = tk.Menu(self.parent)

        self.file_menu = tk.Menu(self.menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.catch_destroy)

        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.parent.config(menu=self.menu)

        self.chosen_file = tk.StringVar()

        self.frame2 = ttk.Frame(self.parent, padding=5, borderwidth=2, relief="sunken", height=50, width=50)
        self.frame2.grid(row=1, column=0, **self.padding)
        self.file_label = ttk.Label(self.frame2)
        self.file_label.grid(column=0, row=0, **self.padding)

    def catch_destroy(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.parent.destroy()

    def open_file(self):
        # Can run file dialogue from anywhere
        chosen_file = filedialog.askopenfilename(filetypes=(("Python files", "*.py"),
                                                            ("Text files", "*.txt"),
                                                            ("Markdown files", "*.md;*.mkd"),
                                                            ("All files", "*.*") ))
        self.chosen_file.set(chosen_file)
        self.file_label["text"] = self.chosen_file.get()

        # print("You pressed File->Open\n{}".format(chosen_file))


def main():
    root = tk.Tk()

    root.withdraw()
    my_file = filedialog.askopenfilename()
    messagebox.showinfo("Title text", f"You chose {my_file}")
    # Show window again
    root.deiconify()

    MyGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
