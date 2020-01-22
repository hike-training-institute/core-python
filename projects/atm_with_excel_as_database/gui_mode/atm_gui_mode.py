from tkinter import Tk, Frame, Entry, Button, Label, END
from atm_gui_utils import validate_user, check_balance, deposit_amount, withdraw_amount


def get_entry(*enteries):
    """
    accepts any number of Tkinter Entries
    :param enteries: Tkinter Entries
    :return: list of values in Tkinter Entry Widget
    """
    return [entry.get() for entry in enteries]

# ------------------------------------------------Actions----------------------------------------------------------

def login_action(welcome_frame, user_name_entry, user_password_entry):
    """
    function for login button
    :param welcome_frame: Tkinter Frame
    :param user_name_entry: Tkinter Entry
    :param user_password_entry: Tkinter Entry
    :return: Validates the username and password
    """

    input_username, input_password = get_entry(user_name_entry, user_password_entry)
    validation, user_position = validate_user(input_username, input_password)
    print(validation, user_position)
    if validation:
        welcome_frame.pack_forget()
        show_atm_functionalities_frame(welcome_frame, input_username, user_position)
    else:
        failed_validation_label = Label(welcome_frame, text="Provided username and password is Invalid !!!")
        failed_validation_label.grid(row=3, column=0)

def cancel_login_action(welcome_frame, user_name_entry, user_password_entry):
    """
    Fucntion for Cancel button
    :param welcome_frame: Tkinter Frame Object
    :param user_name_entry: Tkinter Entry Object
    :param user_password_entry: Tkinter Entry Object
    :return: clears the Tkinter Entries
    """
    for entry in [user_name_entry, user_password_entry]:
        entry.delete(0, END)
    welcome_frame.winfo_children()[-1].destroy()

# ------------------------------------------------Actions---------------------------------------------------------


# ---------------------------------------------------Frames-----------------------------------------------------------
def show_welcome_frame(gui):
    """
    Creates Welcome Frame for ATM Replica
    :param gui:
    :return:
    """

    welcome_frame = Frame(master=gui)

    #Frame Elements:
    user_name_label = Label(welcome_frame, text="Enter Your UserName :")
    user_password_label = Label(welcome_frame, text="Enter Your Password :")
    user_name_entry = Entry(welcome_frame)
    user_password_entry = Entry(welcome_frame)
    login_buttion = Button(welcome_frame, text="Login",
                           command=lambda : login_action(welcome_frame, user_name_entry, user_password_entry))
    cancel_button = Button(welcome_frame, text='Cancel',
                           command=lambda : cancel_login_action(welcome_frame, user_name_entry, user_password_entry))

    #Element Positions :
    user_name_label.grid(row=0)
    user_name_entry.grid(row=0, column=1)
    user_password_label.grid(row=1)
    user_password_entry.grid(row=1, column=1)
    login_buttion.grid(row=2, column=0)
    cancel_button.grid(row=2, column=1)
    welcome_frame.pack()


def show_atm_functionalities_frame(welcome_frame, username, user_position):
    """
    Creates atm_func_frame
    :param welcome_frame: Tkinter Frame
    :param username: str
    :param user_position: str
    :return: Atm functionalities
    """

    global user_balance
    user_balance = ""

    gui = welcome_frame.master
    atm_func_frame = Frame(gui)

    #Frame Elements
    welcome_user_label = Label(atm_func_frame, text=f"Hi {username} Welcome")


    balance_entry = Entry(atm_func_frame, text="current Balance...")
    balance_label = Label(atm_func_frame, text = 'click to check Balance')
    balance_button = Button(atm_func_frame, text='Check Balance',
                            command=lambda: check_balance(user_position, balance_entry))
    deposit_label = Label(atm_func_frame, text="Enter Deposit Amount")
    deposit_entry = Entry(atm_func_frame)
    deposit_button = Button(atm_func_frame, text='Deposit Amount',
                            command=lambda : deposit_amount(deposit_entry.get(), user_position))
    withdraw_label = Label(atm_func_frame, text='Enter Withdraw Amount')
    withdraw_entry = Entry(atm_func_frame)
    withdraw_button = Button(atm_func_frame, text = 'Withdraw Amount',
                             command=lambda : withdraw_amount(withdraw_entry.get(), user_position))
    #Element Position:
    welcome_user_label.grid(row=0, column=1)
    balance_label.grid(row=1, column=1)
    balance_entry.grid(row=1, column=2)
    balance_button.grid(row=1, column=3)
    deposit_label.grid(row=2, column=1)
    deposit_entry.grid(row=2, column=2)
    deposit_button.grid(row=2, column=3)
    withdraw_label.grid(row=3, column=1)
    withdraw_entry.grid(row=3, column=2)
    withdraw_button.grid(row=3, column=3)
    atm_func_frame.pack()

# ---------------------------------------------------Frames-----------------------------------------------------------

# ---------------------------------------------------Main Functions----------------------------------------------------

def create_gui(gui):
    """
    Creates ATM GUI
    :param gui:
    """
    gui.title("ATM REPLICA")
    gui.minsize(500, 200)
    show_welcome_frame(gui)


if __name__ == "__main__":
    gui = Tk(baseName='Atm Machine Replica...')
    create_gui(gui)
    gui.mainloop()