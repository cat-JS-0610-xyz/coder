from tkinter import *
encrypt_for_copy = " "
crypt = 1
choice = 1 
kitten_made_encrypt = ""
kitten_made_decrypt = ""
e1_but_lower = ""
reverse_list = []
listt = []
original = []
code = []
code2= []
code3= []
file  = open('language.txt', 'r')
original_text = open('original.txt', 'r')
code_text = open('code_1.txt', 'r')
code2_text = open('code_2.txt', 'r')
code3_text = open('code_3.txt', 'r')
language = file.read(1)
original = original_text.read()
code = code_text.read()
code2 = code2_text.read()
#code3 = code3_text.read()
original.append("\n")
code.append("\n")
code2.append("\n")
#code3.append("\n")
def choice_1():
    global choice
    choice = 1
    b2['state'] = 'active'
def choice_2():
    global choice
    choice = 2
    b2['state'] = 'active'
def choice_3():
    global choice
    choice = 3
    b2['state'] = 'active'
def choice_caesar():
    global choice
    choice = "caesar"
    b2['state'] = 'active'
def reverse_choice():
    global choice
    choice = "reverse"
    b2['state'] = 'disabled'
def crypt_action():
    global e1, original, code,code2, encrypt_for_copy, crypt, language, choice, kitten_made_encrypt, kitten_list,kitten_made_decrypt,reverse_list, e1_but_lower
    kitten_made_encrypt = ""
    if len(e1.get()) != 0:
        if crypt == 1:
            if choice == 1:
                e1_but_lower = e1.get()
                e1_but_lower = e1_but_lower.lower()
                for kitten_is_making_encrypt in e1_but_lower    :
                    index = original.index(kitten_is_making_encrypt)
                    kitten_made_encrypt = kitten_made_encrypt + code[index]
                kitten_made_encrypt = "Ā" + kitten_made_encrypt
            if choice == 2:
                for kitten_is_making_encrypt in e1.get():
                    index = original.index(kitten_is_making_encrypt)
                    kitten_made_encrypt = kitten_made_encrypt + code2[index]
                kitten_made_encrypt = "ġ" + kitten_made_encrypt
            if choice == 3:
                for kitten_is_making_encrypt in e1.get():
                    index = original.index(kitten_is_making_encrypt)
                    kitten_made_encrypt = kitten_made_encrypt + code3[index]
                kitten_made_encrypt = kitten_made_encrypt + "܀"

            if choice == "caesar":
                kitten_made_encrypt = kitten_made_encrypt + "ϔ"
                for kitten_is_making_encrypt in e1.get():   
                    index = original.index(kitten_is_making_encrypt)
                    if index != 58 and index != 32 and index != 77 and index != 78:
                        kitten_made_encrypt = kitten_made_encrypt + original[index+1]
                    elif index == 58:
                        kitten_made_encrypt = kitten_made_encrypt + "a"
                    elif index == 32:
                        kitten_made_encrypt = kitten_made_encrypt + "а"
                    elif index == 77:
                        kitten_made_encrypt = kitten_made_encrypt + "1"
                    elif ingex == 78:
                        kitten_made_encrypt = kitten_made_encrypt + "\n"
            if choice == "reverse":
                reverse_list = []
                kitten_made_encrypt = e1.get()
                for step in range(len(kitten_made_encrypt)):
                    reverse_list.append(kitten_made_encrypt[step])
                reverse_list.reverse()
                reverse_list.append("ɚ")#܀ ண
                kitten_made_encrypt = ""
                for step in range(len(reverse_list)):
                    kitten_made_encrypt = kitten_made_encrypt + reverse_list[step]
            l3.configure(text = kitten_made_encrypt)
            encrypt_for_copy = kitten_made_encrypt
        #1:Ā 2: 3:܀ ġ Caesar:ϔ reverse:ɚ
        elif crypt == 2:
            kitten_made_decrypt = ""
            kitten_made_encrypt = e1.get()
            if kitten_made_encrypt[0] == "Ā":
                for kitten_is_making_encrypt in kitten_made_encrypt[1:len(kitten_made_encrypt)]:
                    index = code.index(kitten_is_making_encrypt)
                    kitten_made_decrypt = kitten_made_decrypt + original[index]
            
            elif kitten_made_encrypt[0] == "ġ":
                for kitten_is_making_encrypt in kitten_made_encrypt[1:len(kitten_made_encrypt)]:
                    index = code2.index(kitten_is_making_encrypt)
                    kitten_made_decrypt = kitten_made_decrypt + original[index]
                    
            elif kitten_made_encrypt[0] == "ϔ":
                for kitten_is_making_encrypt in kitten_made_encrypt[1:len(kitten_made_encrypt)]:
                    index = original.index(kitten_is_making_encrypt)
                    if index != 0 and index != 33 and index != 59 and index != 78:
                        kitten_made_decrypt = kitten_made_decrypt + original[index-1]
                    elif index == 0:
                        kitten_made_decrypt = kitten_made_decrypt + "я"
                    elif index == 33:
                        kitten_made_decrypt = kitten_made_decrypt + "z"
                    elif index == 59:
                        kitten_made_decrypt = kitten_made_decrypt + " "
                    elif ingex == 78:
                        kitten_made_decrypt = kitten_made_decrypt + "\n"
            elif kitten_made_encrypt[len(kitten_made_encrypt)-1] == "ɚ":
                kitten_made_encrypt = kitten_made_encrypt[0:len(kitten_made_encrypt)-1]
                reverse_list = []
                for step in range(len(kitten_made_encrypt)):
                    reverse_list.append(kitten_made_encrypt[step])
                reverse_list.reverse()
                kitten_made_decrypt = ""
                for step in range(len(reverse_list)):
                    kitten_made_decrypt = kitten_made_decrypt + reverse_list[step]
                    
            elif kitten_made_encrypt[len(kitten_made_encrypt)-1] == "܀":
                for kitten_is_making_encrypt in kitten_made_encrypt[0:len(kitten_made_encrypt)-1]:
                    index = code3.index(kitten_is_making_encrypt)
                    kitten_made_decrypt = kitten_made_decrypt + original[index]
            #add third cyper
            l3.configure(text = kitten_made_decrypt)
            encrypt_for_copy = kitten_made_decrypt
def rus():
    global language,file, choicemenu
    file.close()
    file = open('language.txt', 'w')
    file.write("1")
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
    mainmenu.entryconfigure(1, label='Файл')
    mainmenu.entryconfigure(2, label='Шифр')
    mainmenu.entryconfigure(3, label='Язык')
    mainmenu.entryconfigure(4, label='Помощь')
    filemenu.entryconfigure(0, label='Открыть"Большой режим"')
    choicemenu.entryconfigure(0, label='Шифр один')
    choicemenu.entryconfigure(1, label='Шифр два')
    choicemenu.entryconfigure(2, label='Шифр три')
    choicemenu.entryconfigure(4, label='Шифр Цезаря')
    choicemenu.entryconfigure(5, label='Обратный текст')
    choicemenu.entryconfigure(7, label='Добавить шифр...')
    helpmenu.entryconfigure(0, label='Справка')
    helpmenu.entryconfigure(1, label='Связь с разработчиком')
    file.close()
def eng():
    global language,file
    file.close()
    file = open('language.txt', 'w')
    file.write("0")
    language = 0
    l1.config(text="Write a text")
    if crypt == 1:
        b1.config(text="encrypt")
        l2.config(text="Encrypted text")
    elif crypt == 2:
        b1.config(text="decrypt")
        l2.config(text="Decrypted text")
    b2.config(text="code table")
    rb1.config(text="crypt_action")
    rb2.config(text="decrypting")
    b3.config(text="copy to clipboard")
    mainmenu.entryconfigure(1, label='File')
    mainmenu.entryconfigure(2, label='Cyper')
    mainmenu.entryconfigure(3, label='Language')
    mainmenu.entryconfigure(4, label='Help')
    filemenu.entryconfigure(0, label='Open"Big mode"')
    choicemenu.entryconfigure(0, label='Cipher one')
    choicemenu.entryconfigure(1, label='Cipher two')
    choicemenu.entryconfigure(2, label='Cipher trhee')
    choicemenu.entryconfigure(4, label="Caesar's cyper")
    choicemenu.entryconfigure(5, label='Reverse cyper')
    choicemenu.entryconfigure(7, label='Add cipher...')
    helpmenu.entryconfigure(0, label='Reference')
    helpmenu.entryconfigure(1, label='Bond with orginator')
    file.close()
#root
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
#menu
filemenu = Menu(mainmenu, tearoff=0)
choicemenu = Menu(mainmenu, tearoff=0)
langmenu = Menu(mainmenu, tearoff=0)
helpmenu = Menu(mainmenu, tearoff=0)
#cypres
choicemenu.add_command(label="Cipher one", command = choice_1)
choicemenu.add_command(label="Cipher two", command = choice_2)
choicemenu.add_command(label="Cipher trhee", command = choice_3)
choicemenu.add_separator()
choicemenu.add_command(label="Caesar's cyper", command = choice_caesar)
choicemenu.add_command(label="Reverse cyper", command = reverse_choice)
choicemenu.add_separator()
choicemenu.add_command(label="Add cipher...")
#language
langmenu.add_command(label="English", command = eng)
langmenu.add_command(label="Русский", command = rus)
#help
helpmenu.add_command(label="Reference")
helpmenu.add_command(label="Bond with orginator")
#file(don't work)
filemenu.add_command(label='Open "Big mode"')
#menu more
mainmenu.add_cascade(label="File", menu=filemenu)
mainmenu.add_cascade(label="Cipher", menu=choicemenu)
mainmenu.add_cascade(label="Language", menu=langmenu)
mainmenu.add_cascade(label="Help", menu=helpmenu)
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
        for step in range(0,len(original)-3):
            textInput = textInput + original[step] + " = " + code[step] + "\n"
        if language == 0: 
            textInput = textInput + "apostrophe = ☯" + "\n"
            textInput = textInput + "space = Ѩ" + "\n"
        elif language == 1:
            textInput = textInput + "апостроф = ☯" + "\n"
            textInput = textInput + "пробел = Ѩ" + "\n"
    elif choice == 2:
        for step in range(0,len(code2)-3):
            textInput = textInput + original[step] + " = " + code2[step] + "\n"
        if language == 0:
            textInput = textInput + "apostrophe = Ŵ" + "\n"
            textInput = textInput + "space = Ѭ" + "\n"
        elif language == 1:
            textInput = textInput + "апостроф = Ŵ" + "\n"
            textInput = textInput + "пробел = Ѭ" + "\n"
    elif choice == 3:
        for step in range(0,len(code3)-3):
            textInput = textInput + original[step] + " = " + code3[step] + "\n"
        if language == 0:
            textInput = textInput + "apostrophe = ã" + "\n"
            textInput = textInput + "space = B" + "\n"
        elif language == 1:
            textInput = textInput + "апостроф = ã" + "\n"
            textInput = textInput + "пробел = B" + "\n"
    elif choice == "caesar":
        for step in range(0,len(code2)-4):
            if step != 58 and step != 32:
                textInput = textInput + original[step] + " = " + original[step+1] + "\n"
            elif step == 58:
                textInput = textInput + "z = a" + "\n"
            elif step == 32:
                textInput = textInput + "а = я" + "\n"
        if language == 0:
            textInput = textInput + ") = apostrophe" + "\n"
            textInput = textInput + "apostrophe = space" + "\n"
            textInput = textInput + "space = 1" + "\n"
        if language == 1:
            textInput = textInput + ") = апостроф" + "\n"
            textInput = textInput + "апостроф = пробел" + "\n"
            textInput = textInput + "пробел = 1" + "\n"
    text.config(font=("Courier", 10, 'bold'))
    text.insert(1.0,textInput)
    scroll = Scrollbar(table, command=text.yview)
    scroll.pack(side=LEFT, fill=Y)
    text.configure(state='disabled')
    text.config(yscrollcommand=scroll.set)
    
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
def copy():
    root.clipboard_clear()
    root.clipboard_append(encrypt_for_copy)

#interface
root.resizable(False, False)
l1 = Label(text="Write a text")
l1.config(font=("Verdana", 15, 'bold'))
e1 = Entry(width=22)
e1.config(font=("Calibri", 13))
b1 = Button(text="encrypt", padx = 60,command = crypt_action)
b2 = Button(text="code table", padx = 48,command = show_all)
b1.config(font=("Verdana", 12, 'bold'))
b2.config(font=("Verdana", 12, 'bold'))
l2 = Label(text="Encrypted text")
l2.config(font=("Verdana", 15, 'bold'))
l3 = Label(text = "",width=22, bg = "white")
l3.config(font=("Calibri", 13))
rb1 = Radiobutton(text="crypt_action", variable=var, value=0, command = enn)
rb2 = Radiobutton(text="decrypting", variable=var, value=1, command = dee)
b3 = Button(text="copy to clipboard", padx = 75,command = copy)
b3.config(font=("Verdana", 12, 'bold'))
#event

#position
l1.pack()
e1.pack()
b1.place(x=200,y=76,anchor=CENTER)
b2.place(x=200,y=112,anchor=CENTER)
rb1.place(x=150,y=130)
rb2.place(x=150,y=150)
l2.place(x=200,y=182,anchor=CENTER)
l3.place(x=98,y=200)
b3.place(x=200,y=250,anchor=CENTER)
if language == "0":
    eng()
elif language == "1":
    rus()
root.mainloop()
file.close()
