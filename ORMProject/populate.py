import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ORMProject.settings')
import django
django.setup()


# Generating fake data for EmployeeModel
from myapp.models import EmployeeModel
from faker import Faker
f=Faker()
def populate_date(n):
    for i in range (n):
        ename = f.name()
        email =f.email()
        city =f.address()
        address=f.address()
        company=f.company()
        salary=f.random_int(min=10000,max=70000)
        jobrole=f.job()

        EmployeeModel.objects.create(ename=ename,email=email,city=city,address=address,company=company,salary=salary,jobrole=jobrole)

n = int(input("Enter the no. of records...."))
populate_date(n)
print(f"{n} no of records created sucessfully")


