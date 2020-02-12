from tkinter import*
root = Tk()


def callback():
    print("Click!")
button1 = Button(root, text="One", command=callback, bg="Red", fg="Green")
button2 = Button(root, text="Two", command=callback, bg="Red", fg="Green")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
print("Screen Width: ", w)
print("Screen Height: ", h)
root.geometry(str(w) + "x" + str(h))

button1.place(x=200, y=200)
button2.place(x=500, y=500)
