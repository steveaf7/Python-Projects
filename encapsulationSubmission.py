
# create class myClass
class myClass:
    def __init__(self): 
        self._secret = "I have a secret" #setting a protected variable
        self.__supersecret = "This one is really secret" #setting the value of a private variablee

    # to show private variable
    def exposeVar(self):
        print("__supersecret = {}".format(self.__supersecret))

    #to change private variable
    def changeVar(self, value):
        self.__supersecret = value

this = myClass()
print("_secret = {}".format(this._secret))
this._secret = "Now it is exposed"
print("_secret = {}".format(this._secret))
this.exposeVar()
this.changeVar("Now it's not so secret")
this.exposeVar()
##print(this.__supersecret) # this would cause an error because __supersecret is a private variable
        
