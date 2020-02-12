from tkinter import*
root = Tk()


def callback(event):
    print("click at", event.x, event.y)
frame = Frame(root, width=100, height=100)
frame.bind("<Button>", callback)
frame.pack()
root.mainloop()
