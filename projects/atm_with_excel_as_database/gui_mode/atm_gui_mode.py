from tkinter import Tk, Frame, Entry, Button, Label, END, PhotoImage

from atm_gui_frames import *
from tkinter import font



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

    gui = Tk(baseName='Atm Machine Replica...' )
    bg_image = PhotoImage(file='/home/nandagopal/hti/core-python/projects/atm_with_excel_as_database/gui_mode/atm_image.png')
    label_for_image = Label(gui, image=bg_image, **label_configs)
    label_for_image.pack()
    gui.configure(background=gui_bg)
    create_gui(gui)
    gui.mainloop()