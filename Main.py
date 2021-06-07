import tkinter as tk
from GUI import App

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Compilers Scanner Project")
    root.geometry("990x490")
    app = App(root)
    app.mainloop()










""" from Scanner import Scanner
sc = Scanner()

sc.scan('''
{ Sample program in TINY language – computes factorial
}
read x; {input an integer }
if 0 < x then { don’t compute if x <= 0 }
fact := 1;
repeat 
fact := fact * x;
x := x - 1
until x = 0;
write fact { output factorial of x }
end

''')
print(sc.table)
 """
