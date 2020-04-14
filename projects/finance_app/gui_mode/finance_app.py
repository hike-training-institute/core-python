from tkinter import Tk, Frame, Entry, Button, Label
from utils.db_utils import cursor
from utils.queries import login_validate_query

def validate_user(username, password):
    db_result = cursor.execute(login_validate_query.format(username, password))
    return True if db_result else False


def login(frame, username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    print("Entered Username and Password :", username, password)
    validate_user(username, password)


def func():
    print("Welcome...")

if __name__ == '__main__':
    gui = Tk(baseName='Finance App')

    #Frame
    welcome_frame = Frame(master=gui, borderwidth=10, padx=100, pady=100)

    #Frame Components
    welcome_label = Label(welcome_frame, text = 'Hike Institute Finance App', font=('Helvetica', 18, 'bold') )
    username_label = Label(welcome_frame, text='Enter Your Username :')
    password_label = Label(welcome_frame, text='Enter Your Password :')
    username_entry = Entry(welcome_frame, borderwidth=4)
    password_entry = Entry(welcome_frame, borderwidth=4)
    login_button = Button(welcome_frame, text='login',command=lambda: login(welcome_frame, username_entry, password_entry))

    #positions
    welcome_label.grid(row=0)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1)
    login_button.grid(row=3)


    #Packing the elements
    welcome_frame.pack()

    gui.minsize(500, 200)
    gui.mainloop()



