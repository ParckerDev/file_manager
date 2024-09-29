import tkinter

window = tkinter.Tk()
window.title('File Manager')
window.geometry('350x350')
window.resizable(False, False)
text = tkinter.Label(window, text='File', background='silver', width=10)
text.grid(column=1, row=1)
button_select =tkinter.Button(window, text='open file', background='silver', width=10)
button_select.grid(column=1, row=2)

window.mainloop()