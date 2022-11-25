#class creation || Attribute types ||
class Employee:
    #class attribute
    orgName="Persistent"
    #Instance attribute
    def __init__(self,id, name, baseLoc):
        self.id=id
        self.name=name
        self.baseLoc=baseLoc
    #instance method
    def info(self):
        print("Employee details: name= {} id= {}company= {}".format(self.name, self.id, Employee.orgName))

    def getEmp(self):
        return self

    def setEmpName(self,name):
        self.name = name

    def setEmpId(self,id):
        self.id = id

    def setEmpId(self,baseLoc):
        self.baseLoc=baseLoc

    #class method
    @classmethod
    def orgName(cls,orgName):
        cls.orgName=orgName

    #static method
    @staticmethod
    def companyQuote():
        print("See Beyond and Rise Above")