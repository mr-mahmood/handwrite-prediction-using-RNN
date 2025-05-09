from front import gui
from tkinter import *
# My own codes import
import directory


def persian_alphabet():
    address = '.'
    info = {}
    info['name'] = 'persian_alphabet'
    info['img_temp'] = address + directory.persian_alphabet_temp_img
    info['database_Mine'] = address + directory.my_persian_alphabet_dataset
    info['h5'] = address + directory.hand_write_persian_alphabet
    root.destroy()
    a = gui(info)
    a.start()


def persian_number():
    address = '.'
    info = {}
    info['name'] = 'persian_number'
    info['img_temp'] = address + directory.persian_number_temp_img
    info['database_Mine'] = address + directory.my_persian_number_dataset
    info['h5'] = address + directory.hand_write_persian_number
    root.destroy()
    a = gui(info)
    a.start()


color1 = 'white'
color2 = 'BLACK'
root = Tk()
root.title("start")
root.geometry('300x400')
root.resizable(width=False, height=False)  # user cant resize window

main_frame = Frame(root, bg=color2, pady=40)
main_frame.place(relwidth=1, relheight=1)

b2 = Button(
    main_frame,
    background=color2,
    foreground=color1,
    width=15,
    height=2,
    cursor='hand2',
    text='persian alphabet',
    font=('Arial', 16, 'bold'),
    command=persian_alphabet,
)

b3 = Button(
    main_frame,
    background=color2,
    foreground=color1,
    width=15,
    height=2,
    cursor='hand2',
    text='persian number',
    font=('Arial', 16, 'bold'),
    command=persian_number,
)

b1.place(x=50, y=0)
b2.place(x=50, y=110)
b3.place(x=50, y=220)

root.mainloop()
