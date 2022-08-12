
from tkinter import StringVar, ttk

import Employee
import main_frame


def create_frame(frame):
    
    value = []
    for x in Employee.Employee.emp_list:
        value.append(f"{x.name}, {x.emp_id}")
    value.sort()
    
    emp_select_var = StringVar()
    emp_selector = ttk.Combobox(frame,textvariable=emp_select_var,values=value)
    select_label = ttk.Label(frame,text="Employee:")
    
    
    del_bttn = ttk.Button(frame,text="Delete", command=lambda : del_emp())
    back_bttn = ttk.Button(frame,text="Cancel",command=lambda : back())
    
    select_label.grid(column=0,row=0)
    emp_selector.grid(column=1,row=0)
    
    del_bttn.grid(column=0,row=1)
    back_bttn.grid(column=1,row=1)
    
    def del_emp():
        name = emp_select_var.get()
        name = name.split(",")[0]
        employee = Employee.Employee.query_employee(name)
        if employee != None:
            Employee.Employee.emp_list.remove(employee)
            del employee
        back()
        
    def back():
        main_frame.create_frame(frame)
        
