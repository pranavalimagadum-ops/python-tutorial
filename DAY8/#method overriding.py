#method overriding 
class Rbi:
    def homeLoan_ROI(self):
        print("Home Loan Rate og interest =7.5%")
        
    def carLoan(self):
        print("car loan rate of interest= 8%")
class sbi(Rbi):
    def homeloan_ROI(self):
        print("Home loan rate of interest= 6.5%")
obj= sbi()
obj.homeLoan_ROI()
obj.carLoan()