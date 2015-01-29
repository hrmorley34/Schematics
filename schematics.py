class StringVar:
    def __init__(self,value=None):
        self._val=value
    def set(self,value):
        self._val=value
    def get(self):
        return(self._val)

class Schematic:
    def __init__(self):
        " Create Schematic for testing test points "
        self._tps={}
    def New_Test_Point(self,point_name,var):
        " Create a new test point "
        self._tps[point_name]=var
    def Run(self,runcode,outputcommand=print):
        " Execute runcode then print all the test points "
        while True:
            # Running Objects
            exec(runcode)
            # Test Points
            for x in self._tps:
                outputcommand(x+' = '+str(self._tps[x].get()))

def And(a,b,q):
    if a.get() and b.get():
        q.set(True)
    else:
        q.set(False)
def Or(a,b,q):
    if a.get() or b.get():
        q.set(True)
    else:
        q.set(False)
def Xor(a,b,q):
    if a.get() != b.get():
        q.set(True)
    else:
        q.set(False)
def Not(a,q):
    q.set(not a.get())
def Nand(a,b,q):
    c=StringVar()
    And(a,b,c)
    Not(c,q)
def Nor(a,b,q):
    c=StringVar()
    Or(a,b,c)
    Not(c,q)
def Xnor(a,b,q):
    c=StringVar()
    Xor(a,b,c)
    Not(c,q)
def Print_Example():
    print('''import schematics as sch
e=sch.Schematic()
a=sch.StringVar()
b=sch.StringVar(True)
a.set(False)
q=sch.StringVar()
e.New_Test_Point('Q',q)
e.Run("And(a,b,q)\na.set(not a.get())")''')
