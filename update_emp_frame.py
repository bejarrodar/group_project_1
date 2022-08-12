
from tkinter import StringVar, ttk

import Employee
import main_frame


def create_frame(frame):
    
    def handle(_):
        x = emp_select_var.get()
        split = x.split(",")
        employee = Employee.Employee.query_employee(split[0])
        if employee != None:
            name_var.set(employee.name)
            salary_var.set(employee.salary)
            dept_var.set(employee.department.dep_name)
    
    emp_select_var = StringVar()
    emp_selector = ttk.Combobox(frame,textvariable=emp_select_var)
    select_label = ttk.Label(frame,text="Employee:")
    
    value = []
    for x in Employee.Employee.emp_list:
        value.append(f"{x.name}, {x.emp_id}")
    value.sort()
        
    emp_selector["values"] = value
    
    emp_selector.bind("<<ComboboxSelected>>", handle)
    
    name_label = ttk.Label(frame, text="Employee Name:")
    salary_label = ttk.Label(frame, text="Employee Salary:")
    dept_label = ttk.Label(frame,text="Department Name:")
    
    name_var = StringVar()
    salary_var = StringVar()
    dept_var = StringVar()
    
    name_entry = ttk.Entry(frame,textvariable=name_var)
    salary_entry = ttk.Entry(frame,textvariable=salary_var)
    dept_entry = ttk.Entry(frame,textvariable=dept_var)
    
    update_bttn = ttk.Button(frame,text="Update", command=lambda : update_emp())
    back_bttn = ttk.Button(frame,text="Cancel", command=lambda : back())
    
    select_label.grid(column=0,row=0)
    emp_selector.grid(column=1,row=0)
    
    name_label.grid(column=0,row=1)
    name_entry.grid(column=1,row=1)
    salary_label.grid(column=0,row=2)
    salary_entry.grid(column=1,row=2)
    dept_label.grid(column=0,row=3)
    dept_entry.grid(column=1,row=3)
    
    update_bttn.grid(column=0,row=4)
    back_bttn.grid(column=1,row=4)

    def update_emp():
        name = name_var.get()
        salary = salary_var.get()
        dept = dept_var.get()
        department = Employee.Department.query_dept(dept)
        employee_obj = Employee.Employee.query_employee(name)
        try:
            salary = int(salary)
        except:
            print("You probably didn't enter a number")
        employee_obj.department = department
        employee_obj.salary = salary
        employee_obj.name = name
    
    def back():
        main_frame.create_frame(frame)   
        

        
    
    
    