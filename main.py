from tkinter import * 
pwd = "ayaan@3210"

#window setting
root = Tk()
root.geometry("900x500")
root.resizable(False, False)
root.configure(bg='#1ddb79')
button_COLOR = "#d91c6e"

#pages => frames

def start():
    title_var=StringVar()
    text_var=StringVar()
    def new():
        for i in root.winfo_children():
            i.destroy()
        heading = Frame(root, width=400, height=300,background="#d1dce3",highlightbackground="black",highlightthickness=5)
        heading.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.1, anchor="c")
        txt = Label(heading, text='TITLE:',bg="#d1dce3",font=("Tahoma", 22, "bold"))
        txt.place(anchor="e",relx=0.2, rely=0.5, relwidth=0.2, relheight=0.9)
        title_entry=Entry(heading, textvariable = title_var, font = ("Tahoma", 18, "bold"))
        title_entry.place(anchor="c",relx=0.55, rely=0.55, relwidth=0.7, relheight=0.75)
        
        view_btn=Button(heading,text = ' OK ', command = view,font=("Tahoma", 13, "bold"),bg=button_COLOR,fg="#f2f5f7")
        view_btn.place(anchor="w",relx=0.91, rely=0.57, relwidth=0.08, relheight=0.7)

        main = Frame(root, width=400, height=300,background="#d1dce3",highlightbackground="black",highlightthickness=5)
        main.place(relx=0.5, rely=0.6, relwidth=0.8, relheight=0.75, anchor="c")

        text_entry=Entry(main, textvariable = text_var, font = ("Tahoma", 18, "bold"))
        text_entry.grid( padx=10, pady=10, sticky="EW",columnspan=9)
    def view():
        pass
    #getting a clean slate
    for i in root.winfo_children():
        i.destroy()

    heading = Frame(root, width=300, height=300,background="#d1dce3",highlightbackground="black",highlightthickness=5)
    heading.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.1, anchor="c")
    txt = Label(heading, text='CHOOSE',bg="#d1dce3",font=("Tahoma", 22, "bold"))
    txt.place(anchor="c",relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9)


    main = Frame(root, width=300, height=300,background="#d1dce3",highlightbackground="black",highlightthickness=5)
    main.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.5, anchor="c")

    new_btn=Button(main,text = 'NEW', command = new,font=("Tahoma", 22, "bold"),bg=button_COLOR,fg="#f2f5f7")
    new_btn.place(anchor="c",relx=0.5, rely=0.28, relwidth=0.7, relheight=0.4)

    view_btn=Button(main,text = 'VIEW', command = view,font=("Tahoma", 22, "bold"),bg=button_COLOR,fg="#f2f5f7")
    view_btn.place(anchor="c",relx=0.5, rely=0.7, relwidth=0.7, relheight=0.4)

def login():
    def submit():
        passw = passw_var.get()
        passw_var.set("")
        if passw == pwd:
            start()


    #getting a clean slate
    for i in root.winfo_children():
        i.destroy()

    passw_var=StringVar()

    heading = Frame(root, width=300, height=300,background="#d1dce3",highlightbackground="black",highlightthickness=5)
    heading.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.1, anchor="c")
    txt = Label(heading, text='LOGIN',bg="#d1dce3",font=("Tahoma", 22, "bold"))
    txt.place(anchor="c",relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9)

    # main stuff
    main = Frame(root, width=300, height=300,background="#d1dce3",highlightbackground="black",highlightthickness=5)
    main.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.5, anchor="c")

    enter_text = Label(main, text='ENTER PASSWORD ',bg="#8f9da6",font=("Tahoma", 22, "bold"),anchor='center')
    enter_text.place(anchor="se",relx=1, rely=0.35, relwidth=1, relheight=0.35)

    passw_entry=Entry(main, textvariable = passw_var, font = ("Tahoma", 22, "bold"), show = '*')
    passw_entry.place(anchor="c",relx=0.5, rely=0.58, relwidth=0.7, relheight=0.22)

    sub_btn=Button(main,text = 'Submit', command = submit,font=("Tahoma", 18, "bold"),bg=button_COLOR,fg="#faf566")
    sub_btn.place(anchor="c",relx=0.5, rely=0.85, relwidth=0.2, relheight=0.15)


start()
root.mainloop()