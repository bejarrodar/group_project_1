import tkinter
from tkinter import StringVar, ttk

import Employee


def create_frame(frame):
    W = tkinter.W
    
    label_var = []
    label_list = []
    emp_list = Employee.Employee.emp_list
    pages = int(len(emp_list)/ 10)
    current_page = 0
     
    for x in range(10):
        label_var.append(StringVar())
        label_list.append(ttk.Label(frame,textvariable=label_var[x]))
        label_list[x].grid(column=0,row=x+1,sticky=W,columnspan=4)
    
    for y in range(10):
        label_var[y].set(emp_list[y])
        
    id_sort_bttn = ttk.Button(frame,text="ID", command= lambda : sort_id())
    name_sort_bttn = ttk.Button(frame,text="Name", command= lambda : sort_name())
    salary_sort_bttn = ttk.Button(frame,text="Salary", command= lambda : sort_salary())
    date_sort_bttn = ttk.Button(frame,text="Date", command= lambda : sort_date())
    
    id_sort_bttn.grid(column=0,row=0)
    name_sort_bttn.grid(column=1,row=0)
    salary_sort_bttn.grid(column=2,row=0)
    date_sort_bttn.grid(column=3,row=0)
        
    nxt_bttn = ttk.Button(frame,text="Next",command= lambda: nxt_set())
    last_bttn = ttk.Button(frame,text="Last",command= lambda:  last_set())
    
    nxt_bttn.grid(column=3,row=12)
    last_bttn.grid(column=0,row=12,sticky=W)
    
    def nxt_set():
        nonlocal current_page
        if current_page < pages-1:
            for y in range(10*current_page,10*(current_page+1)):
                label_var[y%10].set(emp_list[y])
            current_page += 1
    
    def last_set():
        nonlocal current_page
        if current_page > 0:
            for y in range(10*(current_page-1),10*(current_page)):
                label_var[y%10].set(emp_list[y])
            current_page -= 1
            
    def sort_id():
        nonlocal emp_list
        nonlocal current_page
        emp_list.sort(key=lambda employee: employee.emp_id)
        current_page = 0
        for y in range(10):
            label_var[y].set(emp_list[y])
    
    def sort_name():
        nonlocal emp_list
        nonlocal current_page
        emp_list.sort(key=lambda employee: employee.name)
        current_page = 0
        for y in range(10):
            label_var[y].set(emp_list[y])
    
    def sort_salary():
        nonlocal emp_list
        nonlocal current_page
        emp_list.sort(key=lambda employee: employee.salary)
        current_page = 0
        for y in range(10):
            label_var[y].set(emp_list[y])
    
    def sort_date():
        nonlocal emp_list
        nonlocal current_page
        emp_list.sort(key=lambda employee: employee.date_employ)
        current_page = 0
        for y in range(10):
            label_var[y].set(emp_list[y])
