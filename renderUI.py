import database
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

def renderMain():
    window = tk.Tk()
    window.title("Mythical Tennis")
    rows, columns = database.getTable()
    treeview = ttk.Treeview(window, columns=columns, show="headings")

    # create table
    for col in columns:
        treeview.heading(col, text=col)
    for row in rows:
        treeview.insert("", "end", values=row)

    treeview.pack(side="top", fill="both", expand=True)

    # create the buttons
    frame = Frame(window)
    create = tk.Button(frame, text="Create", command=lambda: create_form(window), height=5, width=20)
    edit = tk.Button(frame, text="Edit", command=lambda: editEntry(window,treeview.item(treeview.focus())["values"][0],treeview.item(treeview.focus())["values"][1],treeview.item(treeview.focus())["values"][2],treeview.item(treeview.focus())["values"][3]), height=5, width=20)
    delete = tk.Button(frame, text="Delete", command=lambda: deleteEntry(window,treeview.item(treeview.focus())["values"][0]), height=5, width=20)
    play = tk.Button(frame, text="Play Match", command=lambda:matchForm(window), height=5, width=20)
    history = tk.Button(frame, text="Past Matches", command=lambda: renderHistory(window), height=5, width=20)
    create.pack(side="left", padx=10, pady=10)
    edit.pack(side="left", padx=10, pady=10)
    delete.pack(side="left", padx=10, pady=10)
    play.pack(side="left", padx=10, pady=10)
    history.pack(side="left", padx=10, pady=10,)

    frame.pack(side="bottom")

    window.mainloop()
def create_form(window):
    form_window = Toplevel(window)
    form_window.minsize(400, 200)
    title= Label(form_window, text="Create a new Character")
    label_name = Label(form_window, text="Name:")
    entry_name = Entry(form_window)
    label_type = Label(form_window, text="Type:")
    entry_type = Entry(form_window)
    label_attack = Label(form_window, text="Attack:")
    entry_attack = Entry(form_window)
    label_defense = Label(form_window, text="Defense:")
    entry_defense = Entry(form_window)
    button_submit = Button(form_window, text="Submit", command=lambda: submitCreate(window,form_window,entry_name.get(), entry_type.get(), entry_attack.get(), entry_defense.get()))

    # Pack the label and entry
    title.pack()
    label_name.pack()
    entry_name.pack()
    label_type.pack()
    entry_type.pack()
    label_attack.pack()
    entry_attack.pack()
    label_defense.pack()
    entry_defense.pack()
    button_submit.pack()

def submitCreate(origin,window, name, type, attack, defense):
    database.create(name, type, attack, defense)
    window.destroy()
    origin.destroy()
    renderMain()

def deleteEntry(origin, id):
    print(id)
    database.delete(id)
    origin.destroy()
    renderMain()

def editEntry(window, name, type, attack, defense):
    form_window = Toplevel(window)

    title = Label(form_window, text="Update Existing Character")
    label_name = Label(form_window, text="Name: "+name)
    label_type = Label(form_window, text="Type:")
    entry_type = Entry(form_window)
    entry_type.insert(0, type)
    label_attack = Label(form_window, text="Attack:")
    entry_attack = Entry(form_window)
    entry_attack.insert(0, attack)
    label_defense = Label(form_window, text="Defense:")
    entry_defense = Entry(form_window)
    entry_defense.insert(0, defense)
    button_submit = Button(form_window, text="Submit", command=lambda: submitUpdate(window,form_window,name, entry_type.get(), entry_attack.get(), entry_defense.get()))

    # Pack the label and entry
    title.pack()
    label_name.pack()
    label_type.pack()
    entry_type.pack()
    label_attack.pack()
    entry_attack.pack()
    label_defense.pack()
    entry_defense.pack()
    button_submit.pack()

def submitUpdate(origin,window, name, type, attack, defense):
     database.update(name, type, attack, defense)
     window.destroy()
     origin.destroy()
     renderMain()

def renderHistory(window):
    form_window = Toplevel(window)
    form_window.minsize(400, 200)

    rows, columns = database.getHistory()
    treeview = ttk.Treeview(form_window, columns=columns, show="headings")

    # create table
    for col in columns:
        treeview.heading(col, text=col)
    for row in rows:
        treeview.insert("", "end", values=row)

    treeview.pack(side="top", fill="both", expand=True)

def matchForm(window):
    form_window = Toplevel(window)
    form_window.minsize(400, 200)

    selected1 = StringVar(form_window)
    selected2 = StringVar(form_window)
    selected1.set("Select Home Player")
    selected2.set("Select Away Player")
    characters = database.getCharacters()
    print(characters)
    characters1 = characters[:]  # create a copy of the list
    characters2 = characters[:]  # create a copy of the list

    form1 = OptionMenu(form_window, selected1, *characters1)
    form1.pack(side="top", fill="both", expand=True, padx=10, pady=10)
    form2 = OptionMenu(form_window, selected2, *characters2)
    form2.pack(side="top", fill="both", expand=True, padx=10, pady=10)

    button_play = Button(form_window, text="Play",command=lambda:submitMatch(window, form_window,selected1.get(),selected2.get()), height=5, width=20)
    button_play.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)

def submitMatch(origin,window,home, away):
    database.playMatch(home, away)
    window.destroy()
    origin.destroy()
    renderMain()