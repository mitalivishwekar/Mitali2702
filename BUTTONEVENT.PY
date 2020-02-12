from tkinter import*
root = Tk()


def callback():
    print("Click!")
button1 = Button(root, text="One", command=callback, bg="Green", fg="Green")
button2 = Button(root, text="Two", command=callback, bg="Red", fg="Green")
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
