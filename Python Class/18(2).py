class Company:
    def company_name(self):
        return 'Google'


class Employee(Company):
    def info(self):
        c_name = super().company_name()
        print("Jessa works at", c_name)


emp = Employee()
emp.info()
