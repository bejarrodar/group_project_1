
from tkinter import StringVar, ttk

import add_emp_frame
import query_frame
import remove_emp_frame
import search_date
import search_dept
import search_manager
import search_name
import search_salary
import update_emp_frame


def create_frame(frame):
    
    for child in frame.winfo_children():
        child.destroy()
    
    add_button = ttk.Button(frame,text="Add Employee", command=lambda : add_emp(frame))
    update_button = ttk.Button(frame,text="Update Employee", command=lambda : update_emp(frame))
    remove_button = ttk.Button(frame, text="Remove Employee", command=lambda : remove_emp(frame))
    query_button = ttk.Button(frame,text="Query Employee", command=lambda : query_emp(frame))
    salary_button = ttk.Button(frame, text="Search by Salary", command=lambda: search_sal(frame))
    date_button = ttk.Button(frame, text="Search by Date", command = lambda: search_date_fun(frame))
    id_button = ttk.Button(frame, text="Search by id/name", command = lambda: search_name_id(frame))
    department_button = ttk.Button(frame, text="Search by department", command= lambda: search_department(frame))
    manager_button = ttk.Button(frame, text="Search by manager", command= lambda: search_man(frame))

    add_button.grid(column=0,row=0)
    update_button.grid(column=0,row=1)
    remove_button.grid(column=1,row=0)
    query_button.grid(column=1,row=1)
    salary_button.grid(column=0, row= 2)
    date_button.grid(column=1, row=2)
    id_button.grid(column=0, row= 3)
    department_button.grid(column=1, row=3)
    manager_button.grid(column=0, row=4)

    def clear_frame(frame):
        for child in frame.winfo_children():
            child.destroy()
    
    def add_emp(frame):
        clear_frame(frame)
        add_emp_frame.create_frame(frame)
    
    def update_emp(frame):
        clear_frame(frame)
        update_emp_frame.create_frame(frame)
    
    def remove_emp(frame):
        clear_frame(frame)
        remove_emp_frame.create_frame(frame)
    
    def query_emp(frame):
        clear_frame(frame)
        query_frame.create_frame(frame)

    def search_sal(frame):
        clear_frame(frame)
        search_salary.create_frame(frame)

    def search_date_fun(frame):
        clear_frame(frame)
        search_date.create_frame(frame)

    def search_name_id(frame):
        clear_frame(frame)
        search_name.create_frame(frame)

    def search_department(frame):
        clear_frame(frame)
        search_dept.create_frame(frame)

    def search_man(frame):
        clear_frame(frame)
        search_manager.create_frame(frame)
