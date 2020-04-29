from tkinter import Tk, Frame, Entry, Button, Label, END, PhotoImage

username = 'nandha'
password = 'nanda123'

def login(username, password):
    print(username, password)

def func():
    print("Welcome...")

if __name__ == '__main__':
    gui = Tk(baseName='Finance App')

    #Frame
    welcome_frame = Frame(master=gui, borderwidth=10, padx=100, pady=100)

    #Frame Components
    welcome_label = Label(welcome_frame, text = 'Hike Institute Finance App', font=('Helvetica', 18, 'bold') )
    user_name_entry = Entry(welcome_frame, borderwidth=4)
    login_button = Button(welcome_frame, text='login',command=lambda: login(username, password))

    #positions
    welcome_label.grid(row=0)
    user_name_entry.grid(row=0, column=1)
    login_button.grid(row=0, column=2)


    #Packing the elements
    welcome_frame.pack()

    gui.minsize(1000, 400)
    gui.title("Basic Tkinter App")
    gui.mainloop()



