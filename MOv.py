class parent():
    def fees(self):
        print("fees paying")
class child(parent):
    a="movies"
    def fees(self):
        print("movies")
c=child()
c.fees()
print("this is a variable",c.a)
    
