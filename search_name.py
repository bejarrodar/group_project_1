import tkinter
from tkinter import StringVar, ttk

import Employee


def create_frame(frame):
    
    search_name_label = ttk.Label(frame, text="Name:")
    search_id_label = ttk.Label(frame, text="ID:")
    
    search_name_var = StringVar()
    search_id_var = StringVar()
    
    search_name_entry = ttk.Entry(frame,textvariable=search_name_var)
    search_id_entry = ttk.Entry(frame, textvariable=search_id_var)
    
    search_name_bttn = ttk.Button(frame, text="Search", command= lambda : search_name())
    search_id_bttn = ttk.Button(frame, text="Search", command= lambda : search_id())
    
    search_name_label.grid(column=0,row=0)
    search_id_label.grid(column=0,row=1)
    search_name_entry.grid(column=1,row=0)
    search_id_entry.grid(column=1,row=1)
    search_name_bttn.grid(column=2,row=0)
    search_id_bttn.grid(column=2,row=1)
    
    
    output_var = StringVar()
    output_label = ttk.Label(frame,textvariable=output_var)
    output_label.grid(column=0,row=2,columnspan=4)
    
    def search_name():
        emp_name = search_name_var.get()
        employee = Employee.Employee.query_employee(emp_name)
        output_var.set(employee)
    
    def search_id():
        emp_id = search_id_var.get()
        try:
            emp_id = int(emp_id)
        except ValueError:
            print("Couldn't understand")
        employee = Employee.Employee.query_id(emp_id)
        output_var.set(employee)
    
