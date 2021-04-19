from tkinter import *
original = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
code =["×","Ø","Þ","Ԡ","Ӝ","Հ","Ԕ","Ԫ","ݚ","ᴂ","ݿ","ᴂ","⁜","₮","₡","₯","₱","₪","₻","₧","‰","₷","₫","₰","ℳ","►","ꝑ","Ꝣ","ꝟ","ꭗ","ﮰ","₳","₨"]
def show_all():
    table = Toplevel()
    table.geometry('330x330+400+300')
    table['bg'] = 'grey'
    text = Text(table ,width=39, height=21)
    text.place_forget()
    text.place(x=14, y=0)
    textInput = ""
    text.delete(1.0,"end")
    #for 
    scroll = Scrollbar(table, command=text.yview)
    scroll.pack(side=LEFT, fill=Y)
    text.config(yscrollcommand=scroll.set)
root = Tk()
root.geometry('400x220+200+100')
root.title("coder")
root.resizable(False, False)
l1 = Label(text="Write a text")
l1.config(font=("Verdana", 15, 'bold'))
e1 = Entry(width=22)
e1.config(font=("Calibri", 13))
b1 = Button(text="encrypt", padx = 60)
b2 = Button(text="code table", padx = 48,command = show_all)
b1.config(font=("Verdana", 12, 'bold'))
b2.config(font=("Verdana", 12, 'bold'))
l2= Label(text="Encrypted code")
l2.config(font=("Verdana", 15, 'bold'))
l3 =Label(text = "",width=22, bg = "white")
l3.config(font=("Calibri", 13))
l1.pack()
e1.pack()
b1.place(x=99,y=60)
b2.place(x=99,y=95)
l2.place(x=112,y=135)
l3.place(x=98,y=165)
root.mainloop()
