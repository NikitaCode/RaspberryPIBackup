import tkinter


window = tkinter.Tk()
widnow.title("LED Control")
window.geometry("300x300")
window.wm_iconbitmap('favicon.ico')


lbl = tkinter.Label(window, text="Label")
ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="Button")

lbl.pack()
ent.pack()
btn.pack()
window.mainloop()