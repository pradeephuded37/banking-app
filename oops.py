class bank:
    bname ='sbi'
    roi = 14
    loc = 'banglore'
    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.bal=c


    def display(self):
        print('name :',self.name)
        print('age :',self.age)
        print('bal :',self.bal)
        print('bname :',self.bname)
        print('roi :',self.roi)
        print('loc :',self.loc)

        print('---'*10)
        
    def deposit(self,amt=0):
        if amt==0:
            amt=self.get_amt()
        self.bal=self.add(self.bal,amt)
        print('deposite done successfully for',self.name,'of',amt)

        print('---'*10)    

    def withdraw(self,amt):
        if amt==0:
            amt=self.get_amt()
        if self.bal>=amt:
            self.bal=self.sub(self.bal,amt)
            print('withdraw done successfully for',self.name,'of',amt)

            print('---'*10)
        else :
            print('insufficient bal:',self.bal)

            print('---'*10)

    @classmethod
    def dispcls(cls):
        print('bname :',cls.bname)
        print('roi :',cls.roi)
        print('loc :',cls.loc)

        print('---'*10)

    @classmethod
    def modify_roi(cls,new_roi):
        cls.roi = new_roi
        print("modification done ",new_roi)
        print('--'*30)

    @classmethod
    def modify_bname(cls,new_bname):
        cls.bname = new_bname
        print("modification done ",new_bname)
        print('--'*30)

    @staticmethod
    def add(a,b):
        return a+b 

    @staticmethod
    def sub(a,b):
        return a-b 

    @staticmethod
    def get_amt():
        a=int("enter amout")
        return a


class bank_update1(bank):
    ifsc = 'SBIB0000833'
    pincode = 580003

    def __init__(self,a,b,c,d,e):
        super().__init__(a,b,c)
        self.email=d
        self.phno=e

    def display(self):
        super().display()
        print("email :",self.email)
        print("phno :",self.phno)

pradeep= bank('pradeep',25,100)  
pradeep.display()  

pradeep = bank_update1('pradeep',25,100,'pradeephuded37@gmail.com',7204942247)
pradeep.display()



            





