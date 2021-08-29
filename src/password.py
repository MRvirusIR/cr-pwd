from tkinter import *
from random import randint
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog

root = Tk()
root.title('Strong Password')
root.iconbitmap('data/assets/icon/lg.ico')
root.geometry("500x450")

def new_rand ():
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())
    my_password = ''
    for x in range(pw_length):
        my_password += chr(randint(33,126))
        
    pw_entry.insert(0, my_password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

def save():
    fl = [('All Files', '*.*'), 
            ('Text Document', '*.txt')]
    f = filedialog.asksaveasfile(mode='a', filetypes=fl,  defaultextension=".txt")
    if f is None:
        return
    text = str("[" + sc_entry.get() + ":" + " " + pw_entry.get() + "]" + '\n')
    f.write(text)
    f.close()

lf = LabelFrame(root, text="How Many characters?")
lf.pack(pady=20)
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

gf = LabelFrame(root, text="What Software Do You Want?")
gf.pack(pady=20)
sc_entry = Entry(gf, font=("Helvetica", 24))
sc_entry.pack(pady=20, padx=20)

pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text='Get Password', command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

save_button = Button(my_frame, text="Save", command=lambda: save())
save_button.grid(row=0, column=2, padx=10)
root.mainloop()