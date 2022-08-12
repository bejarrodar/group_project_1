import json
from datetime import datetime


class Employee():
    total_emp = 1
    emp_list = []
    
    def __init__(self, name:str, salary:int) -> None:
        self.emp_id = Employee.total_emp
        self.name = name
        self.salary = salary
        Employee.total_emp += 1
        self.date_employ = datetime.today().strftime("%m/%d/%Y")
        Employee.emp_list.append(self)
        self.my_manager = None
        self.department = None

    def change_Depart(self, department):
        if self.department != None:
            self.department.remove_employee(self)
        department.add_employee(self)

    def change_id(self, id:int):
        self.emp_id = id

    def change_date(self, date:str):
        self.date_employ = date

    def add_manager(self,manager):
        if self.my_manager != None:
            self.my_manager.remove_employee(self)
        manager.add_employee(self)

    def remove_dept(self):
        self.department.remove_employee(self)

    def remove_manager(self):
        self.my_manager.remove_employee(self)

    def query_employee(emp_name:str):
        for each in Employee.emp_list:
            if each.name.lower() == emp_name.lower():
                return each
        return None

    def __str__(self) -> str:
        outputString = f'ID:{self.emp_id},  Name:{self.name},  Manager:{self.my_manager.name},  Dept:{self.department},  Salary:{self.salary},  Date Joined:{self.date_employ}'
        return outputString
    
    def query_id(emp_id:int):
        for each in Employee.emp_list:
            if each.emp_id == emp_id:
                return each
        return None
    
    def return_dict(self):
        return {"ID":self.emp_id,"Name":self.name,"Manager":self.my_manager.name,"Dept":self.department.dep_name,"Salary":self.salary,"Date":self.date_employ}
    

class Department():
    dept_list = []
    def __init__(self, dep_name):
        self.num_emp = 0
        self.dep_name = dep_name
        self.emp_list = []
        Department.dept_list.append(self)
        
    def add_employee(self,employee:Employee):
        self.emp_list.append(employee)
        employee.department = self
        self.num_emp += 1

    def remove_employee(self,employee:Employee):
        if employee in self.emp_list:
            self.emp_list.remove(employee)
            print("Employee removed from list")
            employee.department = None
            self.num_emp -= 1
        else:
            print("Employee not found in list")
    
    def set_dept_manager(self,manager):
        self.dept_manager = manager
        
    def query_dept(dept_name:str):
        for each in Department.dept_list:
            if each.dep_name.lower() == dept_name.lower():
                return each
        return None
    
    def __str__(self):
        return self.dep_name
        
class Manager(Employee):
    manager_lst = []
    def __init__(self, name:str, salary:int, department:Department):
        super().__init__(name,salary)
        self.num_emp = 0
        self.name = name
        self.department = department
        department.set_dept_manager(self)
        self.emp_list = []
        Manager.manager_lst.append(self)
        self.my_manager = self
    
    def add_employee(self, employee:Employee):
        self.emp_list.append(employee)
        employee.my_manager = self
        self.num_emp += 1

    def remove_employee(self, employee:Employee):
        if employee in self.emp_list:
            self.emp_list.remove(employee)
            print("Employee removed from the list")
            employee.my_manager = None
            self.num_emp -=1
        else:
            print("Employee not found in list")
            
    def query_manager(manager_name:str):
        if manager_name != None:
            for each in Manager.manager_lst:
                if each.name.lower() == manager_name.lower():
                    return each
            return None
        return None

    def remove_manager(self):
        for emp_iterator in self.emp_list:
            emp_iterator.remove_manger()
        self.manager_lst.remove(self)
         
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    #def __dict__(self):
    #   return {"ID":self.emp_id, "Name":self.name, "Manager":self.my_manager, "Dept":self.department, "Salary":self.salary, "Date Employed":self.date_employ}
