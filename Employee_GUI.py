import tkinter
from tkinter import ttk

import Employee
import File_Handler
import main_frame


def main(root):
    
    root.title("Group Project 1")
    
    N = tkinter.N
    W = tkinter.W
    E = tkinter.E
    S = tkinter.S
    
    
    mainframe = ttk.Frame(root, padding="5 5 12 12")
    mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    main_frame.create_frame(mainframe)


if __name__ == "__main__":

    sales = Employee.Department("Sales")
    development = Employee.Department("Development")
    marketing = Employee.Department("Marketing")
    File_Handler.Read_File()
    for _ in range(20):
        test = Employee.Employee("test",32555)
        test.change_date("03/12/2020")
        test2 = Employee.Employee("test2",32555)
        test2.change_date("09/30/1999")
        test3 = Employee.Manager("test3",95000,development)
        test.add_manager(test3)
        test2.add_manager(test3)
        development.add_employee(test)
        marketing.add_employee(test2)
    
    root = tkinter.Tk()
    main(root)
    root.mainloop()
    
