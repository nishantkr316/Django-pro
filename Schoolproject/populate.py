import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Schoolproject.settings')
import django
django.setup()


# Generating fake data for EmployeeModel
from studentapp.models import StudentModel
from faker import Faker
f=Faker()
def populate_date(n):
    for i in range (n):
        name = f.name()
        email =f.email()
        city =f.city()
        add=f.address()
        dob=f.numerify()

        StudentModel.objects.create(name=name,email=email,city=city,add=add,dob=dob)

n = int(input("Enter the no. of records...."))
populate_date(n)
print(f"{n} no of records created sucessfully")