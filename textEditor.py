from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

text_editor = Tk()
text_editor.title('Text Editor')
text_editor.geometry('1280x720')

text = Text(text_editor)
text.pack(fill=BOTH, expand=1)

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != '':
        with open(filepath, 'r') as file:
            text_ = file.read()
            text.delete('1.0', END)
            text.insert('1.0', text_)

def save_as():
    global text
    t = text.get('1.0', 'end-1c')
    save_location = filedialog.asksaveasfilename()
    if save_location != '':
        file1 = open(save_location, 'w+')
        file1.write(t)
        file1.close()

def default():
    messagebox.showinfo('Text Editor', 'Will be realised soon')

file_menu = Menu(tearoff=0)
file_menu.add_command(label='Create', command=default)
file_menu.add_command(label='New window', command=default)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Save', command=default)
file_menu.add_command(label='Save as', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=default)

edit_menu = Menu(tearoff=0)
edit_menu.add_command(label='', command=default)

format_menu = Menu(tearoff=0)
format_menu.add_command(label='Wrap', command=default)
format_menu.add_command(label='Font', command=default)

main_menu = Menu()
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)
main_menu.add_cascade(label='Format', menu=format_menu)


text_editor.config(menu=main_menu)
text_editor.mainloop()

