class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybouns = 400
    # totalsalary = 6100

    @property
    def totalsalary(self):
        return self.salary + self.salarybouns
    
    @totalsalary.setter
    def totalsalary(self, val):
        self.totalbonus  = val - self.salary
    
e = Employee()
print(e.totalsalary)
e.totalsalary = 5800
# print(e.totalsalary)
print(e.salary)
print(e.totalbonus)
