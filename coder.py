from tkinter import *
encrypt_for_copy = " "
crypt = 1
choice = 1
language = 0
kitten_made_encrypt = ""
original = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",'1','2','3','4','5','6','7','8','9','0','!','?','"',',','.','(',')',' ']
code =     ["×","Ø","Þ","Ԡ","Ӝ","Հ","Ԕ","Ԫ","ݚ","¶","ݿ","ᴂ","⁜","₮","₡","₯","₱","₪","₻","₧","‰","₷","₫","₰","ℳ","►","ꝑ","Ꝣ","ꝟ","ꭗ","ﮰ","₨","₳", "§", '¿', 'å','ɷ', 'ʥ','ʭ','ʧ','Ѯ', 'Ә', 'Ԭ','֍','♪','אַ','ﷺ','ﻼ','⑫','Ꝋ','Ꜯ','Ꞧ','☏','Ꝿ','ꭚ','ꭐ','ꝃ','ꞗ','Ꝇ','˧','ͳ','Ω','Σ','ϔ','Ͼ','⑤','҈','ӂ','փ','ﬄ','✄','↝','❉','❮','δ','ℬ','Ѩ']
code2=["ͳ", "Ϡ", "Џ", "Ֆ", "ῡ", "ꝩ", "☭", "Ꜽ", "ӡ", "ҩ", "֍", "⅞", "ﻋ", "🔫", "¶", "Ǥ","ǂ","ʨ","ʬ","Ξ","՝","ԏ","ӹ","Ֆ","Ἔ","█","ﻺ","ﷻ","╫","շ","Ѡ","ᴥ","₽","€","﴾","⁴","―","∑","₿","‽","₰","Ꝁ","Ꝙ","∞","¼","Ɠ","«","E","¦","⚓","₽","צ","⭿","۞","ᶑ","ἶ","ⱷ","▒","♯","⤘","⛇","ሎ","≥","Ꞟ",'۩','Ä','ъ','ȸ','Ƿ','🄼','ÿ','✉','ǥ','Ỡ','ℳ','Ѿ','Ѭ']
kitten_list = []
def show_all(): 
    global original, code, choice
    table = Toplevel() 
    table.geometry('330x330+400+300')
    table['bg'] = 'grey'
    text = Text(table ,width=39, height=21)
    text.place_forget()
    text.place(x=14, y=0)
    textInput = ""
    text.delete(1.0,"end")
    table.resizable(False, False)
    if choice == 1:
        for step in range(0,len(original)-1):
            textInput = textInput + original[step] + " = " + code[step] + "\n"
        textInput = textInput + "space = Ѩ" + "\n"
    elif choice == 2:
        for step in range(0,len(code2)-1):
            textInput = textInput + original[step] + " = " + code2[step] + "\n"
        textInput = textInput + "space = Ѭ" + "\n"
    text.insert(1.0,textInput)
    scroll = Scrollbar(table, command=text.yview)
    scroll.pack(side=LEFT, fill=Y)
    text.configure(state='disabled')
    text.config(yscrollcommand=scroll.set)
    
def encrypting():
    global e1, original, code,code2, encrypt_for_copy, crypt, language, choice, kitten_made_encrypt, kitten_list #,l5
    kitten_made_encrypt = ""
    print(e1.get())
    if len(e1.get()) != 0:
        if crypt == 1:
            if choice == 1:
                for kitten_is_making_encrypt in e1.get()+1:
                    index = original.index(kitten_is_making_encrypt)
                    kitten_made_encrypt = kitten_made_encrypt + code[index]
                kitten_made_encrypt = "Ā" + kitten_made_encrypt
            if choice == 2:
                for kitten_is_making_encrypt in e1.get():
                    index = original.index(kitten_is_making_encrypt)
                    kitten_made_encrypt = kitten_made_encrypt + code[index]
                kitten_made_encrypt = "ġ" + kitten_made_encrypt
        #Ā ġ
        elif crypt == 2:
            kitten_made_encrypt = e1.get()
            for kitten_is_makeing_list in range(kitten_made_encrypt):
                kitten_list.append(kitten_made_encrypt[kitten_is_makeing_list])
            print(kitten_list)
            kitten_list.pop(0)
            print(kitten_list)
            if kitten_made_encrypt[0] == "Ā":
                
                kitten_made_encrypt = ""
                for kitten_is_making_encrypt in e1.get()+1:
                    
                    index = code.index(kitten_is_making_encrypt)
                    kitten_made_encrypt = kitten_made_encrypt + original[index]
            elif kitten_made_encrypt[0] == "ġ":
                kitten_made_encrypt = ""
                for kitten_is_making_encrypt in e1.get():
                    index = code2.index(kitten_is_making_encrypt)
                    kitten_made_encrypt = kitten_made_encrypt + original[index]
        l3.configure(text = kitten_made_encrypt)
        encrypt_for_copy = kitten_made_encrypt
        #l5.config(text = "text successfully encrypted")
'''
        if choice == 1:
            if crypt == 1:
                for kitten_is_making_encrypt in e1.get():
                    index = original.index(kitten_is_making_encrypt)
                    kitten_made_encrypt = kitten_made_encrypt + code2[index]
            elif crypt == 2:
                for kitten_is_making_encrypt in e1.get():
                    index = code2.index(kitten_is_making_encrypt)
                    kitten_made_encrypt = kitten_made_encrypt + original[index]
'''
def copy():
    root.clipboard_clear()
    root.clipboard_append(encrypt_for_copy)
    #l5.config(text = "text successfully copyied")
def enn():
    global crypt, language
    crypt = 1
    if language == 0:
        b1.config(text="encrypt")
        l2.config(text="Encrypted text")
    elif language == 1:
        b1.config(text="зашифровать")
        l2.config(text="Зашифрованный текст")
def dee():
    global crypt
    crypt = 2
    if language == 0:
        b1.config(text="decrypt")
        l2.config(text="Decrypted text")
    elif language == 1:
        b1.config(text="расшифровать")
        l2.config(text="Расшифрованный текст")
def choice_1():
    global choice
    choice = 1
    
def choice_2():
    global choice
    choice = 2
    
def choice_3():
    global choice
    choice = 3
    
def rus():
    global language
    language = 1
    l1.config(text="Напишите текст")
    if crypt == 1:
        b1.config(text="зашифровать")
        l2.config(text="Зашифрованный текст")
    elif crypt == 2:
        b1.config(text="расшифровать")
        l2.config(text="Расшифрованный текст")
    b2.config(text="таблица шифров")
    rb1.config(text="зашифровка")
    rb2.config(text="расшифровка")
    b3.config(text="копировать")
def eng():
    global language
    language = 0
    l1.config(text="Write a text")
    if crypt == 1:
        b1.config(text="encrypt")
        l2.config(text="Encrypted text")
    elif crypt == 2:
        b1.config(text="decrypt")
        l2.config(text="Decrypted text")
    b2.config(text="code table")
    rb1.config(text="encrypting")
    rb2.config(text="decrypting")
    b3.config(text="copy to clipboard")
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
helpmenu = Menu(mainmenu, tearoff=0)
choicemenu.add_command(label="Cipher one", command = choice_1)
choicemenu.add_command(label="Cipher two", command = choice_2)
choicemenu.add_command(label="Cipher trhee", command = choice_3)
choicemenu.add_separator()
choicemenu.add_command(label="Add cipher...")

langmenu.add_command(label="English", command = eng)
langmenu.add_command(label="Русский", command = rus)
helpmenu.add_command(label="Reference")
helpmenu.add_command(label="Bond with orginator")

mainmenu.add_cascade(label="Cipher", menu=choicemenu)
mainmenu.add_cascade(label="Language", menu=langmenu)
mainmenu.add_cascade(label="Help", menu=helpmenu)

root.resizable(False, False)
l1 = Label(text="Write a text")
l1.config(font=("Verdana", 15, 'bold'))
e1 = Entry(width=22)
e1.config(font=("Calibri", 13))
b1 = Button(text="encrypt", padx = 60,command = encrypting)
b2 = Button(text="code table", padx = 48,command = show_all)
b1.config(font=("Verdana", 12, 'bold'))
b2.config(font=("Verdana", 12, 'bold'))
l2 = Label(text="Encrypted text")
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
b1.place(x=200,y=76,anchor=CENTER)
b2.place(x=200,y=112,anchor=CENTER)
rb1.place(x=150,y=130)
rb2.place(x=150,y=150)
l2.place(x=200,y=182,anchor=CENTER)
l3.place(x=98,y=200)
b3.place(x=200,y=250,anchor=CENTER)
#l5.place(x=47,y=300)
root.mainloop()
