#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-07
# Author   : flying

class School(object):

    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.stuffs = []

    def enroll(self,stu_obj):
        print('为学员%s 办理注册手续' %stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        self.stuffs.append(staff_obj)
        print('雇佣新员工%s' %staff_obj.name)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class Teacher(SchoolMember):

    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ----info of teacher :%s----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print('%s is teaching course [%s]'%(self.name,self.course))

class Student(SchoolMember):

    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        ----info of student :%s----
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print("%s has paid tuition for $%s"%(self.name,amount))

school = School('老男孩IT','沙河')

t1 = Teacher('old boy',56,'男',200000,'Linux')
t2 = Teacher('Alex',38,'男',3000,'python')

s1 = Student('Cuzn',18,'男',1001,'python')
s2 = Student('Flying',17,'女',1002,'Linux')

t1.tell()
s1.tell()

school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.stuffs)
print(school.students)

school.stuffs[0].teach()

for stu in school.students:
    stu.pay_tuition(5000)
