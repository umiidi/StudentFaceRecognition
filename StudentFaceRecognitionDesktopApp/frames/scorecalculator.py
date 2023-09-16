from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def scorecalculator():
    from app import app
    scorecalculator_frame = Frame(app, bg="blue", width=800, height=600)
    header = Label(scorecalculator_frame, text="Calculator", fg="white", bg="blue", font=("Constantia 30 bold"), width=10, height=1)
    header.place(x = 327, y=10)

    gpalabel = Label()
    semesterlabel = Label()

    def gpa():
        nonlocal semesterlabel, gpalabel, gpabutton, semesterbutton
        semesterbutton.configure(state="active")
        gpabutton.configure(state="disabled")
        semesterlabel.destroy()


        gpalabel = Label(scorecalculator_frame, bg="blue", width=101, height=31)
        gpalabel.place(x=44, y=120)
        entrylabel = Label()
        def showentry(*args):
            nonlocal entrylabel
            n = int(option_menu.get())
            y = 5
            entrylabel.destroy()
            entrylabel = Label(gpalabel, bg="blue", width=90, height=27)
            resultscore = Label(gpalabel, text="Nəticə: " + str(0.00), bg="blue", fg="white", font="Constantia 17 bold",width=20, height=1)
            def changescore(result):
                resultscore.configure(text="Nətice: " + str(result))
            resultscore.place(x=231, y=21)
            def validate_input(new_value):
                return new_value.isdigit() or new_value == ""
            validate_command = scorecalculator_frame.register(validate_input)
            liste = []
            liste2 = []
            for i in range(n):
                Label(entrylabel, text="Ümumi bal:" ,font="Constantia 15 bold", bg="blue", fg="white", width=10, height=1).place(x=5, y=y-3)
                e = Entry(entrylabel, font=("times new roman", 15), bg="white", fg="black", width=13, validate="key", validatecommand=(validate_command, "%P"))
                e.place(x=131, y=y)
                Label(entrylabel, text="Fənnin krediti:" ,font="Constantia 15 bold", bg="blue",fg="white" ,width=13, height=1).place(x=333, y=y-3)
                e2 = Entry(entrylabel, font=("times new roman", 15), bg="white", fg="black", width=13, validate="key", validatecommand=(validate_command, "%P"))
                e2.place(x=495, y=y)
                liste.append(e)
                liste2.append(e2)
                y += 44
            else: 
                def calculate():
                    listscore = []
                    listkredit = []
                    for i in range(len(liste)):
                        if liste[i].get() == "" or liste2[i].get() == "":
                            messagebox.showerror(title="Notification", message="Please fill in all fields")
                            return
                        else:
                            listscore.append(int(liste[i].get())*int(liste2[i].get()))
                            listkredit.append(int(liste2[i].get()))
                    changescore(round(sum(listscore)/sum(listkredit), 2))

                entrylabel.place(x = 37, y=55)
                calculatebutton = Button(entrylabel, text="Hesabla", state="active", fg="black", command=lambda:[calculate()], font="Constantia 17 bold")
                calculatebutton.place(x = 270, y = y)
        ql = Label(gpalabel, text="Fənn sayı:", bg="blue", fg="white", font="Constantia 20 bold", width=8, height=2)
        ql.place(x=255, y=-27)
        option_menu = ttk.Combobox(gpalabel, values=list(range(3, 9)), state="readonly", width=11, height=10)
        option_menu.bind("<<ComboboxSelected>>", showentry)
        option_menu.place(x = 400, y=1)
        option_menu.current(2)
        showentry()

    def semester():
        nonlocal semesterlabel, gpalabel, gpabutton, semesterbutton
        gpabutton.configure(state="active")
        semesterbutton.configure(state="disabled")
        gpalabel.destroy()
        semesterlabel = Label(scorecalculator_frame, bg="blue", width=101, height=31)
        semesterlabel.place(x=44, y=127)

        resultscore = Label(semesterlabel, text="Nəticə: " + str(0.00), bg="blue", fg="white", font="Constantia 20 bold", width=20, height=1)
        def changescore(result):
            resultscore.configure(text="Nəticə: " + str(result))
        resultscore.place(x=200, y=1)
        listquiz = []
        listkol = []
        quizlabel = Label(semesterlabel, bg="blue", width=40, height=11)
        def showquiz(*args):
            nonlocal listquiz
            n = quizsay.get()
            x = 1; y=7
            for i in listquiz:
                i.destroy()
            listquiz.clear()
            for i in range(int(n)):
                listquiz.append(ttk.Combobox(quizlabel, values=list(range(0, 11)), state="readonly", width=10, height=11))
                listquiz[i].place(x = x, y=y)
                listquiz[i].current(0)
                if i == 2 or i == 5: 
                    y+=50
                    x = 1
                else: x+=99
        quizlabel.place(x = 22, y=111)
        Label(semesterlabel, text="Məşğələ ballarının sayı:", bg="blue", fg="white", font="Constantia 15 bold",width=20, height=1).place(x=1, y=70)
        quizsay = ttk.Combobox(semesterlabel, values=list(range(0, 9)), state="readonly", width=10, height=11)
        quizsay.bind("<<ComboboxSelected>>", showquiz)
        quizsay.place(x = 245, y=77)
        quizsay.current(3)        

        kolleklabel = Label(semesterlabel, bg="blue", width=40, height=11)
        def showkollek(*args):
            nonlocal listkol
            n = kolleksayi.get()
            y = 7
            for i in listkol:
                i.destroy()
            listkol.clear()
            for i in range(int(n)):
                listkol.append(ttk.Combobox(kolleklabel, values=list(range(0, 11)), state="readonly", width=17, height=11))
                listkol[i].place(x = 69, y=y)
                listkol[i].current(0)
                y+=50

        kolleklabel.place(x = 400, y=111)

        Label(semesterlabel, text="Kollekvium ballarının sayı:", bg="blue", fg="white", font="Constantia 15 bold",width=22, height=1).place(x=377, y=70)
        kolleksayi = ttk.Combobox(semesterlabel, values=list(range(2, 4)), state="readonly", width=7, height=5)
        kolleksayi.place(x = 647, y=77)
        kolleksayi.bind("<<ComboboxSelected>>", showkollek)
        kolleksayi.current(1)        

        Label(semesterlabel, text="Sərbəst iş balı", bg="blue", fg="white", font="Constantia 17 bold",width=13, height=1).place(x=87, y=300)
        serbestis = ttk.Combobox(semesterlabel, values=list(range(0, 11)), state="readonly", width=18, height=10)
        serbestis.place(x = 115, y=340)
        serbestis.current(0)
        
        Label(semesterlabel, text="Qb saat / Dərs saatı", bg="blue", fg="white", font="Constantia 17 bold",width=17, height=1).place(x=400, y=300)
        qbsaat = ttk.Combobox(semesterlabel, values=list(range(0, 16)), state="readonly", width=13, height=10)
        qbsaat.place(x = 420, y=340)
        qbsaat.current(0)
        
        derssaat = ttk.Combobox(semesterlabel, values=list(range(15, 135, 15)), state="readonly", width=13, height=10)
        derssaat.place(x = 525, y=340)
        derssaat.current(0)
        
        def calculate():
            quiz = [int(i.get()) for i in listquiz]
            kol = [int(i.get()) for i in listkol]
            quizres = round(sum(quiz)*(0.4), 1)
            quizres /= len(quiz)
            kolres = round(sum(kol)*(0.6), 1)
            kolres /= len(kol)

            result1 = round((quizres + kolres)*3, 1)
            result2 = round(10 - (10*int(qbsaat.get()))/int(derssaat.get()), 2)
            result3 = int(serbestis.get())
            result = sum([result1, result2, result3])
            changescore(round(result, 1))
            
        calculatebutton = Button(semesterlabel, text="Hesabla", state="active", fg="black", command=calculate, font="Constantia 17 bold")
        calculatebutton.place(x = 290, y = 400)
        showkollek()
        showquiz()

    gpabutton = Button(scorecalculator_frame, command=gpa, text="UOMG score", font="Constantia 15 bold", bg="white", width=11, height=1)
    gpabutton.place(x=457, y=70)

    semesterbutton = Button(scorecalculator_frame, command=semester, text="Semester score", font="Constantia 15 bold", bg="white", width=13, height=1)
    semesterbutton.place(x=290, y=70)

    gpabutton.invoke()
    cancel = Button(scorecalculator_frame, text="CANCEL", font="Constantia", bg="white", width=7, height=1)
    cancel.configure(command=lambda: [scorecalculator_frame.destroy()])
    cancel.place(x=10, y=10)
    scorecalculator_frame.place(x=0, y=0)
