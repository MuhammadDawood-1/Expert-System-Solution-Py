class zaigham:
    def __init__(self,Name,age,cell_no):
        self.name=Name
        self._age=age #protected
        self.__cell=cell_no #private
    def getcell(self):
        return self.__cell
    def setcell(self):
        return self.__cell
    
    def _info(self):
        return self.name+ "is" +str(self._age) + " his cell no is"+ self.__cell

class ess(zaigham):
    def __init__(self,age,name,cell_no,id):
        super().__init__(name,age,cell_no)
        self.age = age
        self.id =id
    def getdata(self):
        super()._info()
class d(ess):
    def __init__(self,age,name,cell_no,id):
        super().__init__(age,name,cell_no,id)
    def get_data(self):
        return super()._info()
e = d(21,"dawood","03030303",1)

print(e.get_data())




# class fast(zaigham):
#     def __init__(self, Name, age, cell_no,uni,section):
#         super().__init__(Name, age, cell_no)
#         self.university=uni
#         self.sec=section
#         return super()._info()
#         print(self.university)
#         print(self.sec)
    
    
#     f=fast("haha",10,"23332","FASTNU","B")
    