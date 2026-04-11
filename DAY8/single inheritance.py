class College:   #first class  first- level  
  def college_name(self):  
    print("Modern College")   
class Student(College): #second class second - level  
  def student_info(self):  
    print("Name:   Prashant Jha")  
    print("Branch: Mechanical")  
obj = Student()
obj.college_name()
obj.student_info()