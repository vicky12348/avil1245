class a:
    __x=10
    print("this is in claas a",__x)
        
class b(a):
    print(a.x)
obj1=b
obj2=a
print(obj2.x)
    
    

