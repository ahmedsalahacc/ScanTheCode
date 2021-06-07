import tkinter as tk
from tkinter import *
from tkinter import ttk
from Scanner import Scanner


class App(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.frame1 = tk.Frame(master=root, relief=tk.GROOVE,borderwidth=5)
        self.frame2 = tk.Frame(master=root, relief=tk.GROOVE, borderwidth=5)
        self.root.columnconfigure(0, weight=1, minsize=100)
        self.root.columnconfigure(1, weight=1, minsize=100)
        self.root.rowconfigure(0, weight=1, minsize=100)
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        self.create_all()

    def create_all(self):
        self.codebox = self.create_textbox(self.frame1)
        self.codebox.pack(side='top')
        #self.tinycompile = self.create_button(
           # self.frame2, width=5, height=2, text="Scan", command=lambda: print("hello")).pack(side='bottom')
        self.listbox = self.create_table(self.frame2)
        self.showScores = tk.Button(self.frame2, text="Scan",
                               width=15, command=lambda: self.show()).grid(row=4, column=0)
        self.clearBox = tk.Button(self.frame2, text="clear",
                               width=15, command=lambda: self.clear()).grid(row=4, column=1)

    def create_textbox(self, master, background='black', foreground='white'):
        textbox = Text(master, bg=background, fg=foreground)
        return textbox

    def create_button(self, master, text, command, width=2, height=2, color='black', foreground='white'):
        return Button(master, text=text, width=width, height=height, fg=color, command=command)

    def create_table(self, master):

        label = tk.Label(master, text="Results", font=(
            "Arial", 30)).grid(row=0, columnspan=3)
        # create Treeview with 3 columns
        cols = ('Parameter', 'Type')
        listBox = ttk.Treeview(master, columns=cols, show='headings')
        # set column headings
        for col in cols:
            listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        return listBox

    def show(self):
        text = self.codebox.get('1.0','end')
        scanner = Scanner()
        data = scanner.scan(text)
        self.clear_labels()
        if data[:5]!= "ERROR":
            for name, score in data:
                self.listbox.insert("", "end", values=(name, score))
            self.label.destroy()
            self.label = Label(self.frame1, text="Successfully Scanned", fg='green')
            self.label.pack(side='top')
        else:
            words = data.split(' ')
            word = words[1]
            print(word)
            self.label.destroy()
            self.find(word)
            self.label = Label(self.frame1,text=f"{words[0]} {words[1]} at col {words[2]} ", fg='red')
            self.label.pack(side='top')

    def clear(self):
        try:
            self.codebox.destroy()
            self.listbox.destroy()
            self.codebox = self.create_textbox(self.frame1)
            self.codebox.pack(side='top')
            self.listbox = self.create_table(self.frame2)
            if self.label:
                self.label.destroy()
        except:
            pass
        self.clear_labels()

    def clear_labels(self):
        try:
            self.label.destroy()
        except: pass
        self.label = Label(self.frame1, text="Type some TINY  in the black window")
        self.label.pack(side='top')

    def find(self, word):

        #remove tag 'found' from index 1 to END
        self.codebox.tag_remove('found', '1.0', END)

        #returns to widget currently in focus
        s = word
        if s:
            idx = '1.0'
            while 1:
                #searches for desried string from index 1
                idx = self.codebox.search(s, idx, nocase=1,
                                stopindex=END)
                if not idx:
                    break

                #last index sum of current index and
                #length of self.codebox
                lastidx = '%s+%dc' % (idx, len(s))

                #overwrite 'Found' at idx
                self.codebox.tag_add('found', idx, lastidx)
                idx = lastidx

            #mark located string as red
            self.codebox.tag_config('found', foreground='red')



