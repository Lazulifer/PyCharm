import tkinter as tk #Naming convention. "as" let's us call the import something else ("tk")
from functools import wraps
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button


#Creates a simple notepad for me to write text onto, save as a txt file, and load again

#Classes are ways to make "objects", which are blocks of code with their own properties
class SimpleNotepad:
    #Methods are functions that act on objects. Objects

    #Self IS the object you're working with in the class. You give the "self" in the class traits by doing self.etc...
    #root is the main window of the application
    def __init__(self, root: Tk) -> None:
        #Initializers don't return anything. The init method is declared within a class
        #and used to initialize the attributes of an object as soon as the object is formed
        #You don't need to call an init method again for it to work. Double-underlined methods
        #Are called "Magic Methods/Dunder Methods". They're inherent to Python


        self.root = root #Assigning the root to our instance
        self.root.title('Casimir\'s Notepad')

        #Text widget
        self.text_area: Text = Text(self.root, wrap='word')
        #self.root indicates that this is the window we're affecting
        #Wrap makes it so the words make proper new lines instead of splitting weirdly
        self.text_area.pack(expand=True,fill='both')
        #.pack lets us actually put it on a screen
        #expand=true makes sure that the widget takes up the whole screen

        #Button Frame
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack() #Don't forget to put pack

        #Save button
        self.save_button: Button = Button(self.button_frame, text='Save', command=self.save_file)
        #Attached to button frame, not to root, text is "save",
        #command makes pressing the button do something (saving, here)
        self.save_button.pack(side=tk.LEFT)
        #Aligns the save button leftwards of load

        #Load button
        self.load_button: Button = Button(self.button_frame, text='Load', command=self.load_file)
        #Not using () because we're going to call them as methods later
        self.load_button.pack(side=tk.LEFT)

        #DO NOT get used to copy-pasting blocks of code if you think you'll forget to make proper changes


    def save_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(defaultextension='.txt',
                                                      filetypes=[('Text Files', '*.txt')])
        #Searches for .txt by default, and will also look for all files that end in .txt


        with open(file_path, 'w') as file:
        #I absolutely didn't know "with" was a keyword. "w" is write mode
            file.write(self.text_area.get(1.0, tk.END))
            #From beginning to end

        print(f'File saved to: {file_path}')

    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(defaultextension='.txt',
                                                      filetypes=[('Text Files', '*.txt')])

        with open(file_path, 'r') as file:
        #'r' for read mode
            content: str = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, content)

            print(f'File loaded from: {file_path}')

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()


if __name__ == '__main__':
    main()