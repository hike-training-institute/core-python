from tkinter import Tk, Frame, Entry, Button, Label, END, PhotoImage
import food_bill_with_db_class as backend

def login(username, password):
    # print (username, password, sep = "\n")
    count = 1
    abc = backend.Food_bill()
    abc.first(count,username, password)

if __name__ == '__main__':
    gui = Tk(baseName='Foodbill App')

    #Frame
    welcome_frame = Frame(master=gui, borderwidth=10, padx=100, pady=100)

    #Frame Components
    welcome_label = Label(welcome_frame, text = 'Foodbill App', font=('Helvetica', 18, 'bold') )
    user_name_label = Label(welcome_frame, text = 'username', font=('Helvetica', 8, ''))
    user_name_entry = Entry(welcome_frame, borderwidth=4)
    password_label = Label(welcome_frame, text='password', font=('Helvetica', 8, ''))
    password_entry = Entry(welcome_frame, borderwidth=4)
    # username = user_name_entry.get()
    # password = password_entry.get()
    login_button = Button(welcome_frame, text='login',command= lambda: login(user_name_entry.get(), password_entry.get()))

    #positions
    welcome_label.grid(row=0, column=1)
    user_name_label.grid(row=1, column=0)
    password_label.grid(row=2, column=0)
    user_name_entry.grid(row=1, column=1)
    password_entry.grid(row=2, column=1)
    login_button.grid(row=3, column=1)

    #Packing the elements
    welcome_frame.pack()
    #
    # def secondframe():
    #     welcome_frame1 = Frame(master=gui, borderwidth=10, padx=100, pady=100)
    #
    #     # Frame Components
    #     welcome_label = Label(welcome_frame1, text='Foodbill App', font=('Helvetica', 18, 'bold'))
    #     user_name_label = Label(welcome_frame1, text='username', font=('Helvetica', 8, ''))
    #     user_name_entry = Entry(welcome_frame1, borderwidth=4)
    #     password_label = Label(welcome_frame1, text='password', font=('Helvetica', 8, ''))
    #     password_entry = Entry(welcome_frame1, borderwidth=4)
    #     # username = user_name_entry.get()
    #     # password = password_entry.get()
    #     login_button = Button(welcome_frame1, text='login')
    #
    #     # positions
    #     welcome_label.grid(row=0, column=1)
    #     user_name_label.grid(row=1, column=0)
    #     password_label.grid(row=2, column=0)
    #     user_name_entry.grid(row=1, column=1)
    #     password_entry.grid(row=2, column=1)
    #     login_button.grid(row=3, column=1)
    #
    #     # Packing the elements
    #     welcome_frame1.pack()
    #
    #     gui.minsize(500, 200)
    #     gui.mainloop()
