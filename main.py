from tkinter import * 
from tkinter.scrolledtext import ScrolledText
import sqlite3
import hashlib
from datetime import datetime as dt
import helper
#window setting
root = Tk()
root.geometry("900x600")
root.resizable(False, False)
root.configure(bg='#1ddb79')
button_bg = "#d91c6e"
frame_label_bg = "#d1dce3"

conn = sqlite3.connect("Data.db")
curr = conn.cursor()
curr.execute('''
CREATE TABLE IF NOT EXISTS data(
             s_no INTEGER NOT NULL,
             title TEXT NOT NULL,
             text TEXT NOT NULL,
             date TEXT NOT NULL
             )
'''
)
conn.commit()
conn.close()
#pages => frames

def start():
    title_var=StringVar()

    def new():
        for i in root.winfo_children():
            i.destroy()
        heading = Frame(root, width=400, height=300,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
        heading.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.1, anchor="c")
        txt = Label(heading, text='TITLE:',bg=frame_label_bg,font=("Tahoma", 22, "bold"))
        txt.place(anchor="e",relx=0.2, rely=0.5, relwidth=0.2, relheight=0.9)
        title_entry=Entry(heading, textvariable = title_var, font = ("Tahoma", 18, "bold"))
        title_entry.place(anchor="c",relx=0.58, rely=0.52, relwidth=0.8, relheight=0.75)
        
        main = Frame(root, width=400, height=280,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
        main.place(relx=0.5, rely=0.6, relwidth=0.8, relheight=0.75, anchor="c")
        text_entry=ScrolledText(main, font = ("Tahoma", 16, "normal"), height=13, width=60)
        text_entry.grid(padx=10, pady=10, sticky="EW",columnspan=9)

        #back to start page= back
        back_btn=Button(main,text = ' Back ', command = start ,font=("Tahoma", 13, "bold"),bg=button_bg,fg="#f2f5f7")
        back_btn.place(anchor="n",relx=0.35, rely=0.8, relwidth=0.2, relheight=0.15)

        submit_btn=Button(main,text = ' Submit ', command = lambda:submit(text_entry),font=("Tahoma", 13, "bold"),bg=button_bg,fg="#f2f5f7")
        submit_btn.place(anchor="n",relx=0.65, rely=0.8, relwidth=0.2, relheight=0.15)
    
    def submit(text_entry):
            text_var = text_entry.get("1.0", "end-1c") #from 0th char to end -1 (last char is newline char)
            title = title_var.get()
            rn = dt.now()
            if rn.minute >= 10:
                date = f"{rn.day}/{rn.month}/{rn.year} | time: {rn.hour}:{rn.minute}"
            else:
                date = f"{rn.day}/{rn.month}/{rn.year} | time: {rn.hour}:0{rn.minute}"
            con = sqlite3.connect("Data.db")
            cur = con.cursor()
            cur.execute("SELECT s_no FROM data")
            s_no = len(cur.fetchall())
            cur.execute("INSERT INTO Data (s_no,title, text, date) VALUES (?,?,?,?)", (s_no+1,title,text_var,date))
            con.commit()
            con.close()
            start()

    def text_view(heading,data):
        for i in root.winfo_children():
            i.destroy()
        header = Frame(root, width=300, height=300,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
        header.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.1, anchor="c")
        txt = Label(header, text=heading,bg=frame_label_bg,font=("Tahoma", 22, "bold"))
        txt.place(anchor="c",relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9)

        main = Frame(root, width=300, height=350,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
        main.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.5, anchor="c")

        text_entry=ScrolledText(main, font = ("Tahoma", 16, "normal"), height=13, width=60,wrap=WORD)
        #text_entry.grid(padx=10, pady=10, sticky="EW",columnspan=9)
        text_entry.pack()
        text_entry.config(state="normal")
        text_entry.insert("1.0", data)
        text_entry.config(state=DISABLED)
        footer = Frame(root, width=300, height=100,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
        footer.place(relx=0.5, rely=0.88, relwidth=0.7, relheight=0.18, anchor="c")
        back_btn=Button(footer,text = ' Back ', command = start ,font=("Tahoma", 13, "bold"),bg=button_bg,fg="#f2f5f7")
        back_btn.place(anchor="n",relx=0.5, rely=0.3, relwidth=0.7, relheight=0.5)

    def view():
        for i in root.winfo_children():
            i.destroy()
        heading = Frame(root, width=300, height=300,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
        heading.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.1, anchor="c")
        txt = Label(heading, text='VIEW',bg=frame_label_bg,font=("Tahoma", 22, "bold"))
        txt.place(anchor="c",relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9)

        main = Frame(root, width=300, height=350,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
        main.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.5, anchor="c")

        #database stuff
        con = sqlite3.connect("Data.db")
        cur = con.cursor()
        query = "SELECT * FROM data"
        cur.execute(query)
        columns = cur.fetchall()

        sframe = helper.ScrollFrame(main,color="#312C2C")
        for i in range(len(columns)):
            f = Frame(sframe.viewPort, width=450, height=70,background=frame_label_bg,highlightbackground="black",highlightthickness=1)
            f.grid(column=0,row=i)
            helper.PrettyButton(f,label=f"{i+1}. {columns[i][1]}",
                                colors=("black","white","#414141","#F0E10E"),
                                cmd=lambda:text_view(heading=columns[i][1],data=columns[i][2]),relief="flat").get().place(relx=0.01,rely=0.2,relwidth=0.95,relheight=0.6)
            Label(sframe.viewPort,text=columns[i][3],anchor="w",font=("Tahoma",10,"normal")).grid(column=1,row=i)
        sframe.pack(side="top", fill="both", expand=True)

        footer = Frame(root, width=300, height=100,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
        footer.place(relx=0.5, rely=0.88, relwidth=0.7, relheight=0.18, anchor="c")
        back_btn=Button(footer,text = ' Back ', command = start ,font=("Tahoma", 13, "bold"),bg=button_bg,fg="#f2f5f7")
        back_btn.place(anchor="n",relx=0.5, rely=0.3, relwidth=0.7, relheight=0.5)
        con.close()

    #getting a clean slate
    for i in root.winfo_children():
        i.destroy()

    heading = Frame(root, width=300, height=300,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
    heading.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.1, anchor="c")
    txt = Label(heading, text='CHOOSE',bg=frame_label_bg,font=("Tahoma", 22, "bold"))
    txt.place(anchor="c",relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9)


    main = Frame(root, width=300, height=400,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
    main.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.6, anchor="c")

    new_btn=Button(main,text = 'NEW', command = new,font=("Tahoma", 22, "bold"),bg=button_bg,fg="#f2f5f7")
    new_btn.place(anchor="c",relx=0.5, rely=0.28, relwidth=0.7, relheight=0.4)

    view_btn=Button(main,text = 'VIEW', command = view,font=("Tahoma", 22, "bold"),bg=button_bg,fg="#f2f5f7")
    view_btn.place(anchor="c",relx=0.5, rely=0.7, relwidth=0.7, relheight=0.4)

def login():
    def submit():
        passw = passw_var.get()
        passw_var.set("")
        passw = passw.encode()
        passw = hashlib.sha256(passw).hexdigest()
                # creating file path
        dbfile = 'pwd.db'
        # Create a SQL connection to our SQLite database
        con = sqlite3.connect(dbfile)

        # creating cursor
        cur = con.cursor()

        # reading all table names
        table_list = [a for a in cur.execute("SELECT password FROM pwd ")]
        # here is you table list

        # Be sure to close the connection
        
        if passw == table_list[0][0]:
            con.close()
            start()



    #getting a clean slate
    for i in root.winfo_children():
        i.destroy()

    passw_var=StringVar()

    heading = Frame(root, width=300, height=300,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
    heading.place(relx=0.5, rely=0.15, relwidth=0.7, relheight=0.1, anchor="c")
    txt = Label(heading, text='LOGIN',bg=frame_label_bg,font=("Tahoma", 22, "bold"))
    txt.place(anchor="c",relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9)

    # main stuff
    main = Frame(root, width=300, height=300,background=frame_label_bg,highlightbackground="black",highlightthickness=5)
    main.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.5, anchor="c")

    enter_text = Label(main, text='ENTER PASSWORD ',bg="#8f9da6",font=("Tahoma", 22, "bold"),anchor='center')
    enter_text.place(anchor="se",relx=1, rely=0.35, relwidth=1, relheight=0.35)

    passw_entry=Entry(main, textvariable = passw_var, font = ("Tahoma", 22, "bold"), show = '*')
    passw_entry.place(anchor="c",relx=0.5, rely=0.58, relwidth=0.7, relheight=0.22)

    sub_btn=Button(main,text = 'Submit', command = submit,font=("Tahoma", 18, "bold"),bg=button_bg,fg="#faf566")
    sub_btn.place(anchor="c",relx=0.5, rely=0.85, relwidth=0.2, relheight=0.15)

login()
root.mainloop()
