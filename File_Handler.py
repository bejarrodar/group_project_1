import json

import Employee


def Write_File():
    try:
        with open('employee.json','w') as output_file:
            print("Writing Employees to json file...")
            employee_list = Employee.Employee.emp_list
            out_list = []
            for emp in employee_list:
                current_id = emp.emp_id
                current_name = emp.name
                current_salary = emp.salary
                current_dept = emp.department.dep_name
                if emp.my_manager != None:
                    current_manager = emp.my_manager.name
                else:
                    current_manager = None
                current_date = emp.date_employ
                write_dict = {"emp_id":current_id,"name":current_name,"salary":current_salary,
                              "department":current_dept,"manager":current_manager,"date_employ":current_date}
                out_list.append(write_dict)
            json_obj = json.dump(out_list,output_file)
                #output_file.write(json_obj)
    except FileNotFoundError as e:
            print(e)

def Read_File():
    try:
        with open('employee.json','r') as input_file:
            json_obj = json.load(input_file)
            for emp in json_obj:
                current_id = int(emp["emp_id"])
                current_name = emp["name"]
                current_salary = int(emp["salary"])
                current_dept = Employee.Department.query_dept(emp["department"])
                current_manager = Employee.Manager.query_manager(emp["manager"])
                current_date = emp["date_employ"]
                #print(current_manager)
                if current_manager != None:
                    new_employee = Employee.Employee(current_name, current_salary)
                    new_employee.change_Depart(current_dept)
                    new_employee.add_manager(current_manager)
                else:
                    new_employee = Employee.Manager(current_name,current_salary,current_dept)
                new_employee.change_id(current_id)
                new_employee.change_date(current_date)
    except FileNotFoundError as e:
        print(e)
