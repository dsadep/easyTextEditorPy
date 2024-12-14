from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class TextEditor(Tk):
    def __init__(self):
        super().__init__()
        self.title('Text Editor')
        self.geometry('1280x720')

        self.text = Text(self)
        self.text.pack(fill=BOTH, expand=1)

        self.is_saved = True

        self.text.bind("<<Modified>>", self.on_modify)

        self.create_menus()

    def create_menus(self):
        file_menu = Menu(tearoff=0)
        file_menu.add_command(label='New window', command=self.new_window)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label='Save as', command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.destroy_editor)

        edit_menu = Menu(tearoff=0)
        edit_menu.add_command(label='Undo', command=self.default)  # Placeholder for future functionality

        format_menu = Menu(tearoff=0)
        format_menu.add_command(label='Wrap', command=self.default)  # Placeholder for future functionality
        format_menu.add_command(label='Font', command=self.default)  # Placeholder for future functionality

        main_menu = Menu(self)
        main_menu.add_cascade(label='File', menu=file_menu)
        main_menu.add_cascade(label='Edit', menu=edit_menu)
        main_menu.add_cascade(label='Format', menu=format_menu)

        self.config(menu=main_menu)

    def open_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                text_ = file.read()
                self.text.delete('1.0', END)
                self.text.insert('1.0', text_)

    def save_as(self):
        t = self.text.get('1.0', 'end-1c')
        save_location = filedialog.asksaveasfilename()
        if save_location:
            with open(save_location, 'w+') as file1:
                file1.write(t)

    def on_modify(self, event):
        self.is_saved = False
        self.text.edit_modified(False)

    def destroy_editor(self):
        if not self.is_saved:
            if messagebox.askyesno('Closing', 'File is not saved. Are you sure you want to close?'):
                self.destroy()
        else:
            self.destroy()

    def new_window(self):
        NewWindow(self)

    def default(self):
        messagebox.showinfo('Text Editor', 'Will be realized soon')


class NewWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title('New Window')
        self.geometry('1280x720')

        self.text = Text(self)
        self.text.pack(fill=BOTH, expand=1)

        self.is_saved = True

        self.text.bind("<<Modified>>", self.on_modify)

        self.create_menus()

    def create_menus(self):
        file_menu = Menu(tearoff=0)
        file_menu.add_command(label='New window', command=self.new_window)
        file_menu.add_command(label='Open', command=self.parent.open_file)
        file_menu.add_separator()
        file_menu.add_command(label='Save as', command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label='Close', command=self.destroy_editor)

        edit_menu = Menu(tearoff=0)
        edit_menu.add_command(label='Undo', command=self.default)

        format_menu = Menu(tearoff=0)
        format_menu.add_command(label='Wrap', command=self.default)
        format_menu.add_command(label='Font', command=self.default)

        main_menu = Menu(self)
        main_menu.add_cascade(label='File', menu=file_menu)
        main_menu.add_cascade(label='Edit', menu=edit_menu)
        main_menu.add_cascade(label='Format', menu=format_menu)

        self.config(menu=main_menu)

    def open_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as file:
                text_ = file.read()
                self.text.delete('1.0', END)
                self.text.insert('1.0', text_)

    def save_as(self):
        t = self.text.get('1.0', 'end-1c')
        save_location = filedialog.asksaveasfilename()
        if save_location:
            with open(save_location, 'w+') as file1:
                file1.write(t)

    def on_modify(self, event):
        self.is_saved = False
        self.text.edit_modified(False)

    def destroy_editor(self):
        if not self.is_saved:
            if messagebox.askyesno('Closing', 'File is not saved. Are you sure you want to close?'):
                self.destroy()
        else:
            self.destroy()
    def default(self):
        messagebox.showinfo('Text Editor', 'Will be realized soon')

    def new_window(self):
        NewWindow(self)

if __name__ == '__main__':
    app = TextEditor()
    app.mainloop()
