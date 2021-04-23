from tkinter import *
encrypt_for_copy = " "
original = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"," "]
code =     ["×","Ø","Þ","Ԡ","Ӝ","Հ","Ԕ","Ԫ","ݚ","ᴂ","ݿ","ᴂ","⁜","₮","₡","₯","₱","₪","₻","₧","‰","₷","₫","₰","ℳ","►","ꝑ","Ꝣ","ꝟ","ꭗ","ﮰ","₨","₳"," "]
def show_all():
    global original, code
    table = Toplevel()
    table.geometry('330x330+400+300')
    table['bg'] = 'grey'
    text = Text(table ,width=39, height=21)
    text.place_forget()
    text.place(x=14, y=0)
    textInput = ""
    text.delete(1.0,"end")
    for step in range(0,len(original)):
        textInput = textInput + original[step] + " = " + code[step] + "\n"
    text.insert(1.0,textInput)
    scroll = Scrollbar(table, command=text.yview)
    scroll.pack(side=LEFT, fill=Y)
    text.configure(state='disabled')
    text.config(yscrollcommand=scroll.set)
def encrypting():
    global e1, original, code, encrypt_for_copy
    kitten_made_encrypt = ""
    if len(e1.get()) != 0:
        for kitten_is_making_encrypt in e1.get():
            index = original.index(kitten_is_making_encrypt)
            kitten_made_encrypt = kitten_made_encrypt + code[index]
        l3.configure(text = kitten_made_encrypt)
        encrypt_for_copy = kitten_made_encrypt
def copy():
    root.clipboard_append(encrypt_for_copy)
root = Tk()
var = IntVar()
var.set(0)
root.geometry('400x320+200+100')
root.title("coder")
root.resizable(False, False)
l1 = Label(text="Write a text")
l1.config(font=("Verdana", 15, 'bold'))
e1 = Entry(width=22)
e1.config(font=("Calibri", 13))
b1 = Button(text="encrypt", padx = 60,command = encrypting)
b2 = Button(text="code table", padx = 48,command = show_all)
b1.config(font=("Verdana", 12, 'bold'))
b2.config(font=("Verdana", 12, 'bold'))
l2 = Label(text="Encrypted code")
l2.config(font=("Verdana", 15, 'bold'))
l3 = Label(text = "",width=22, bg = "white")
l3.config(font=("Calibri", 13))
rb1 = Radiobutton(text="encrypting", variable=var, value=0,)
rb2 = Radiobutton(text="uncrypting", variable=var, value=1)
b3 = Button(text="copy", padx = 75,command = copy)
b3.config(font=("Verdana", 12, 'bold'))
l1.pack()
e1.pack()
b1.place(x=99,y=60)
b2.place(x=99,y=95)
rb1.place(x=150,y=130)
rb2.place(x=150,y=150)
l2.place(x=112,y=168)
l3.place(x=98,y=200)
b3.place(x=97,y=232)
root.mainloop()
