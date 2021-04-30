from tkinter import *
encrypt_for_copy = " "
crypt = 1
choise = 1
language = 0
original = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",'1','2','3','4','5','6','7','8','9','0','!','?','"',',','.','(',')',' ']
code =     ["×","Ø","Þ","Ԡ","Ӝ","Հ","Ԕ","Ԫ","ݚ","¶","ݿ","ᴂ","⁜","₮","₡","₯","₱","₪","₻","₧","‰","₷","₫","₰","ℳ","►","ꝑ","Ꝣ","ꝟ","ꭗ","ﮰ","₨","₳", "§", '¿', 'å','ɷ', 'ʥ','ʭ','ʧ','Ѯ', 'Ә', 'Ԭ','֍','♪','אַ','ﷺ','ﻼ','⑫','Ꝋ','Ꜯ','Ꞧ','☏','Ꝿ','ꭚ','ꭐ','ꝃ','ꞗ','Ꝇ','˧','ͳ','Ω','Σ','ϔ','Ͼ','⑤','҈','ӂ','փ','ﬄ','✄','↝','❉','❮','δ','ℬ','c']
code2=[]
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
    for step in range(0,len(original)-1):
        textInput = textInput + original[step] + " = " + code[step] + "\n"
    textInput = textInput + "space = Ѩ" + "\n"
    text.insert(1.0,textInput)
    scroll = Scrollbar(table, command=text.yview)
    scroll.pack(side=LEFT, fill=Y)
    text.configure(state='disabled')
    text.config(yscrollcommand=scroll.set)
    
def encrypting():
    global e1, original, code, encrypt_for_copy, crypt #,l5
    kitten_made_encrypt = ""
    if len(e1.get()) != 0:
        if crypt == 1:
            for kitten_is_making_encrypt in e1.get():
                index = original.index(kitten_is_making_encrypt)
                kitten_made_encrypt = kitten_made_encrypt + code[index]

        elif crypt == 2:
            for kitten_is_making_encrypt in e1.get():
                index = code.index(kitten_is_making_encrypt)
                kitten_made_encrypt = kitten_made_encrypt + original[index]
        l3.configure(text = kitten_made_encrypt)
        encrypt_for_copy = kitten_made_encrypt
        #l5.config(text = "text successfully encrypted")
def copy():
    root.clipboard_clear()
    root.clipboard_append(encrypt_for_copy)
    #l5.config(text = "text successfully copyied")
def enn():
    global crypt
    crypt = 1
    b1.config(text="encrypt")
    l2.config(text="Encrypted code")
def dee():
    global crypt
    crypt = 2
    b1.config(text="decrypt")
    l2.config(text="Decrypted code")
def choice_1():
    choise = 1
def choice_2():
    choise = 2
def choice_3():
    choise = 3
def rus():
    language = 1
    l1.config(text="Напишите текст")
    print(language)
    if crypt == 1:
        b1.config(text="зашифровать")
    elif crypt == 2:
        b1.config(text="расшифровать")
def eng():
    language = 0
    l1.config(text="Write a text")
    print(language)
    if crypt == 1:
        b1.config(text="encrypt")
    elif crypt == 2:
        b1.config(text="decrypt")
root = Tk()
var = IntVar()
war = IntVar()
var.set(0)
war.set(0)
root.geometry('400x300+200+100')
root.title("coder")
mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.config(backgroun="black")
mainmenu.add_command(label='File')
#mainmenu.add_command(label='encryption')

choicemenu = Menu(mainmenu, tearoff=0)
langmenu = Menu(mainmenu, tearoff=0)
choicemenu.add_command(label="encription one", command = choice_1)
choicemenu.add_command(label="encription two", command = choice_2)
choicemenu.add_command(label="encription trhee", command = choice_3)
choicemenu.add_separator()
choicemenu.add_command(label="add encription...")
langmenu.add_command(label="english", command = eng)
langmenu.add_command(label="русский", command = rus)
mainmenu.add_cascade(label="encription", menu=choicemenu)
mainmenu.add_cascade(label="language", menu=langmenu)
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
rb1 = Radiobutton(text="encrypting", variable=var, value=0, command = enn)
rb2 = Radiobutton(text="decrypting", variable=var, value=1, command = dee)
b3 = Button(text="copy to clipboard", padx = 75,command = copy)
b3.config(font=("Verdana", 12, 'bold'))
#l4 = Label(text="Like a console")
#l4.config(font=("Verdana", 15, 'bold'))
#l5 = Label(text="", bg = "black",width=23, fg = "white")
#l5.config(font=("Verdana", 15))
l1.pack()
e1.pack()
b1.place(x=99,y=60)
b2.place(x=99,y=95)
rb1.place(x=150,y=130)
rb2.place(x=150,y=150)
l2.place(x=112,y=168)
l3.place(x=98,y=200)
b3.place(x=40,y=232)
#l5.place(x=47,y=300)
root.mainloop()

