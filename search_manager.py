import tkinter
from tkinter import StringVar, ttk

import Employee
import main_frame


def create_frame(frame):
    
    
    W = tkinter.W
    
    search_label = ttk.Label(frame,text="Manager:")
    search_var = StringVar()
    search_entry = ttk.Entry(frame,textvariable=search_var)
    search_bttn = ttk.Button(frame,text="Search", command= lambda : search())
    
    search_label.grid(column=0,row=0)
    search_entry.grid(column=1,row=0)
    search_bttn.grid(column=2,row=0)
    
    nxt_bttn = ttk.Button(frame,text="Next",command= lambda: nxt_set())
    last_bttn = ttk.Button(frame,text="Last",command= lambda:  last_set())
    back_bttn = ttk.Button(frame, text="Back", command= lambda: back())
    
    nxt_bttn.grid(column=3,row=12)
    last_bttn.grid(column=0,row=12,sticky=W)
    back_bttn.grid(column= 5, row =12)
    
    
    output_var = []
    output_list = []
    emp_list = Employee.Employee.emp_list
    pages = int(len(emp_list)/ 10)
    current_page = 0
    
    for x in range(10):
        output_var.append(StringVar())
        output_list.append(ttk.Label(frame,textvariable=output_var[x]))
        output_list[x].grid(column=0,row=x+1,sticky=W,columnspan=4)
    
    def nxt_set():
        nonlocal current_page
        if current_page < pages-1:
            for y in range(10*current_page,10*(current_page+1)):
                try:
                    output_var[y%10].set(emp_list[y])
                except IndexError:
                    pass
            current_page += 1
    
    def last_set():
        nonlocal current_page
        if current_page > 0:
            for y in range(10*(current_page-1),10*(current_page)):
                try:
                    output_var[y%10].set(emp_list[y])
                except IndexError:
                    pass
            current_page -= 1
    
    def search():
        nonlocal output_var
        nonlocal output_list
        nonlocal emp_list
        nonlocal pages
        nonlocal current_page
        
        for y in range(10):
            output_var[y].set("")
        
        manager = Employee.Manager.query_manager(search_var.get())
        if manager != None:
            emp_list = manager.emp_list
        else:
            output_var[0].set("Manager Not Found")
        
        for y in range(10):
            try:
                output_var[y].set(emp_list[y])
            except IndexError:
                print("End of employee list")

    def back():
        main_frame.create_frame(frame)
