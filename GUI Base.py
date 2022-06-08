import tkinter as tk

window = tk.Tk()
window.grid_columnconfigure(0, minsize=100)
window.grid_columnconfigure(1, minsize=100)
window.grid_columnconfigure(2, minsize=100)
window.grid_columnconfigure(3, minsize=100)

#x.geometry('widthXheight+Xpos L/R+Ypos U/D)
window.geometry('400x400+800+200')

##LABEL##
LABLE = tk.Label(text="wingwangchingchang")
LABLE.grid(row=1, column=0)
####


##BUTTON 1##
bt1 = tk.Button(window,
    text="click",
    width=30,
    height=20,
    bg="red",
    fg="yellow",
)
bt1.grid(row=3, column=0)
####


##ENTRY 1##
entry = tk.Entry(
 fg="yellow",
 bg="blue",
 width=50
 )
entry.grid(row=2, column=0)
####


window.mainloop()
