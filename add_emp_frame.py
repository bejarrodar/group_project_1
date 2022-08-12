
from tkinter import StringVar, ttk

import Employee
import main_frame


def create_frame(frame):
    
    name_label = ttk.Label(frame, text="Employee Name:")
    salary_label = ttk.Label(frame, text="Employee Salary:")
    dept_label = ttk.Label(frame,text="Department Name:")
    man_label = ttk.Label(frame, text="Manager:")
    
    name_var = StringVar()
    salary_var = StringVar()
    dept_var = StringVar()
    man_var = StringVar()
    
    value = []
    for x in Employee.Manager.manager_lst:
        value.append(f"{x.name}, {x.emp_id}")
    value.sort()
    
    name_entry = ttk.Entry(frame,textvariable=name_var)
    salary_entry = ttk.Entry(frame,textvariable=salary_var)
    dept_entry = ttk.Entry(frame,textvariable=dept_var)
    man_entry = ttk.Combobox(frame,textvariable=man_var, values=value)
    
    name_label.grid(column=0,row=0)
    name_entry.grid(column=1,row=0)
    salary_label.grid(column=0,row=1)
    salary_entry.grid(column=1,row=1)
    dept_label.grid(column=0,row=2)
    dept_entry.grid(column=1,row=2)
    man_label.grid(column=0, row=3)
    man_entry.grid(column=1, row=3)
    
    create_emp_bttn = ttk.Button(frame,text="Create Employee",command=lambda : create_emp())
    create_man_bttn = ttk.Button(frame,text="Create Manager",command=lambda : create_man())
    back_bttn = ttk.Button(frame,text="Cancel", command=lambda : back())
    
    create_emp_bttn.grid(column=0,row=4)
    create_man_bttn.grid(column=1,row=4)
    back_bttn.grid(column=0,row=5)

    def create_emp():
        name = name_var.get()
        salary = salary_var.get()
        dept = dept_var.get()
        manager = man_var.get()
        department = Employee.Department.query_dept(dept)
        print(department)
        if department != None:
            try:
                salary = int(salary)
            except ValueError:
                print("You probably didn't enter an int")
            employee_obj = Employee.Employee(name, salary)
            employee_obj.add_manager(Employee.Manager.query_manager(manager.split(",")[0]))
            employee_obj.change_Depart(department)
            print(employee_obj)
            back()

    def create_man():
        name = name_var.get()
        salary = salary_var.get()
        dept = dept_var.get()
        department = Employee.Department.query_dept(dept)
        if department != None:
            try:
                salary = int(salary)
            except ValueError:
                print("Failed to create manager")
            else:
                manager = Employee.Manager(name,salary,department)
                print(manager)
                back()

    def back():
        main_frame.create_frame(frame)
