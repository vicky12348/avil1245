class employee:
    a=input("name of the employee")
    def __init__(self,a):
        print("this is constructor",a)
    def sal(self):
        print("hello this is ",self.a)
    @staticmethod
    def m2(a):
        print("this is a static method",a)
    def m3(self,a,b):
        return a+b


obj=employee(2000)
obj1=employee(3000)
obj2=employee(4000)

obj.sal()
employee.m2(obj.m3(2,5))
print("this is the retuen value",obj.m3(2,5))
        
    
