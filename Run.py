import datetime
import sys

import Employee
import File_Handler


def run():
    #Read File
    sales = Employee.Department("Sales")
    development = Employee.Department("Development")
    marketing = Employee.Department("Marketing")
    File_Handler.Read_File()
    #test = Employee.Employee("test",32555)
    #test.change_date("03/12/2020")
    #test2 = Employee.Employee("test2",32555)
    #test2.change_date("09/30/1999")
    #test3 = Employee.Manager("test3",95000,development)
    #test.add_manager(test3)
    #test2.add_manager(test3)
    #development.add_employee(test)
    #marketing.add_employee(test2)
    main()
    #menu
    
    
def main():
    print("Would you like to \n(1)Add \n(2)Update \n(3)Remove \n(4)List Employee Information \n(5)Exit")
    while True:
        try:
            choice = input("What would you like to do? ")
            choice = int(choice)
            break
        except ValueError as e:
            print(e)
    match choice:
        case 1:
            new_emp()
        case 2:
            update_emp()
        case 3:
            remove_emp()
        case 4:
            list_choice = input("""What would you like to list: 
1) All Employees 
2) Employees by salary
3) Employees by salary in range
4) Employees hired in a date range 
5) All employees of a manager
6) Find a single employee(name/id)
7) All employees of a department """)
            try:
                choice_int = int(list_choice)
            except ValueError:
                print("couldn't understand")
            str_list = []
            listEmp = Employee.Employee.emp_list
            for x in listEmp:
                str_list.append(x.return_dict())
            match choice_int:
                case 1:
                    print("Listing all employees:")
                    str_list.sort(key = lambda x: x["ID"])
                    print(str_list)
                    main()
                case 2:
                    empSal = input("List employee salary (low/high): ")[0].lower()
                    if empSal == "l":
                        str_list.sort(key = lambda x: x["Salary"])
                        print(str_list)
                    elif empSal == "h":
                        str_list.sort(key = lambda x: x["Salary"], reverse=True)
                        print(str_list)
                    else:
                        print("Try entering either low or high")
        
                    main()
                case 3:
                    try:
                        salRangeL = input("Please enter the starting salary range (lower): ")
                        salRangeL = int(salRangeL)
                        salRangeH = input("Please enter the ending salary range (higher): ")
                        salRangeH = int(salRangeH)
                    
                        #salRange = [Employee.Employee.salary for Employee.Employee.salary in range(salRangeL,salRangeH)]
                        salRange = [x for x in str_list if x["Salary"] < salRangeH and x["Salary"] > salRangeL]
                        print(salRange)
                    except ValueError as e:
                        print(e)
                    main()
                case 4:
                    low_date = input("What is the starting date you want to search?(MM/DD/YYYY) ")
                    high_date = input("What is the ending date you want to search?(MM/DD/YYYY) ")
                    low_date_obj = datetime.datetime.strptime(low_date,"%m/%d/%Y")
                    high_date_obj = datetime.datetime.strptime(high_date,"%m/%d/%Y")
                    emp_list_in_date = [x for x in str_list if datetime.datetime.strptime(x["Date"],"%m/%d/%Y") > low_date_obj and datetime.datetime.strptime(x["Date"],"%m/%d/%Y") < high_date_obj]
                    print(emp_list_in_date)
                    main()
                case 5:
                    manager_name = input("What manager would you like to see? ")
                    manager = Employee.Manager.query_manager(manager_name)
                    for each in manager.emp_list:
                        print(each.name)
                    main()
                case 6:
                    query = input("What employee would you like to view? ")
                    try:
                        query_int = int(query)
                        employee = Employee.Employee.query_id(query_int)
                        print(employee)
                    except ValueError:
                        employee = Employee.Employee.query_employee(query)
                        print(employee)
                    main()
                case 7:
                    query = input("What department would you like to view? ")
                    department = Employee.Department.query_dept(query)
                    if department != None:
                        for x in department.emp_list:
                            print(x)
                case _:
                    print("I didn't understand")
                    main()
        case 5:
            print("Saving changes to a json file...")
            File_Handler.Write_File()
            print("exiting the program...")
            sys.exit()
        case _:
            main()
            
def new_emp():
    new_choice = input("Would you like to add a manager or regular employee: ")[0].lower()
    if new_choice == "m":
        dept_choice = input("What department is the manager for? ")
        name = input("What is the managers name? ")
        salary = input("What is the managers salary ")
        dept = Employee.Department.query_dept(dept_choice)
        if dept != None:
            new_manager = Employee.Manager(name, salary, dept)
            restart = input("Would you like to add a new employee?(y/n) ")[0].lower()
            if restart == "y":
                new_emp()
            else:
                main()
    elif new_choice == "e":
        dept_choice = input("What department is the employee for? ")
        name = input("What is the employees name? ")
        salary = input("How much does the employee make? ")
        manager_choice = input("Who is this employees manager? ")
        new_employee = Employee.Employee(name, salary)
        manager = Employee.Manager.query_manager(manager_choice)
        if manager != None:
            new_employee.add_manager(manager)
        else:
            print("Manager not in the list")
            new_emp()
        dept = Employee.Department.query_dept(dept_choice)
        if dept != None:
            new_employee.change_Depart(dept)
        else:
            print("The department wasn't in the list")
            new_emp()
        restart = input("Would you like to add a new employee?(y/n) ")[0].lower
        if restart == "y":
            new_emp()
        else:
            main()
    else:
        print("I'm sorry I didn't understand")
        new_emp()

def remove_emp():
    rm_choice = input("Would you like to change a manger or employee(e/m)? ")[0].lower
    if rm_choice == 'm':
        manager_choice = input("What is the name of the manager you'd like to remove? ")
        for x in Employee.Manager.manager_lst: 
            if x.name == manager_choice:
                x.remove_manager()
            else:
                print("Manager not found in the list")
                remove_emp()
    elif rm_choice == 'e':
        employee_choice = input("What is the name of the employee you'd like to remove? ")
        for x in Employee.Employee.emp_list:
            if x.name == employee_choice:
                x.remove_manager
                x.remove_dept()
                x.emp_list._remove(x)
            else:
                print("Employee not found in the list")       
    else:
        print("Invalid input try using e or m")
        rm_choice()

def update_emp():
    #Needs to be coded
    upd_choice = input("Would you like to change the manager or employee ")[0].lower()
    if upd_choice == 'm':
        manager_name = input("What is the name of the manager you'd like to update? ") 
        manager = Employee.Manager.query_manager(manager_name)
        if manager != None:
            input_choice = input("""What would you like to update?
1. Manager Name
2. Manager Salary
3. Department """)
            try:
                int_input = int(input_choice)
            except ValueError:
                print("I didn't understand")
                update_emp()
            match int_input:
                case 1:                
                    newname = input("What is the new name ")
                    manager.name = newname 
                    main()
                case 2:
                    manager_salary = input("What is the new salary ")
                    manager.salary = manager_salary
                    main()
                case 3:
                    manager_department = input("What is the new department you like to go? ")
                    dept = Employee.Department.query_dept(manager_department)
                    if dept != None:
                        manager.department = dept
                    main()
                case _:
                    print("I didn't Understand")
                    update_emp()
        else:
            print("Couldn't find manager")
            update_emp()
    elif upd_choice == 'e':
        employee_name = input("What is the name of the employee you'd like to update? ") 
        employee = Employee.Employee.query_employee(employee_name)
        if employee != None:
            input_choice = input("""What would you like to update?
    1. Employee Name
    2. Employee Salary
    3. Department """)
            try:
                int_input = int(input_choice)
            except ValueError:
                print("I didn't understand")
                update_emp()
            match int_input:
                case 1:                
                    newname = input("What is the new name ")
                    employee.name = newname
                    main() 
                case 2:
                    employee_salary = input("What is the new salary ")
                    employee.salary = employee_salary
                    main()
                case 3:
                    employee_department = input("What is the new department you like to go? ")
                    dept = Employee.Department.query_dept(employee_department)
                    if dept != None:
                        employee.department = dept
                    main()
                case _:
                    print("I didn't Understand")
                    update_emp()
        else:
            print("Couldn't find employee")
            update_emp()
    else:
        print("Invalid input try using e or m")
        update_emp()
        


if __name__ == "__main__":
    run()
    
