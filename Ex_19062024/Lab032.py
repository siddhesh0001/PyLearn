#IMP
# lambda expression
#use to do task in one line

#below formate is normal without lambda
def double_my_salary(salary):
    return salary * 2
print(double_my_salary(1000))

#Below function is using lambda expression

newsalary = lambda salary : salary * 2
print(newsalary(1000))