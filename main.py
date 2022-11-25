from Oops.employee import Employee

e1= Employee(46611,"bishal","Nagpur")
e2=Employee(40011,"Raji","Kolkata")
e2.info()
print(e1.getEmp().name)
e1.setEmpName("V")
print(e1.getEmp().name)
# print("Employee details: name= {} id= {} base={}".format(e1.name,e1.id,e1.baseLoc))