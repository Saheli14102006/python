class Student:
    session='2023-2024'   #class variable, it is shared by all the objects of the class, it is defined inside the class but outside the constructor(__init__), it is accessed by using the class name and the name of the variable, it is used to store the information that is common to all the objects of the class.
    
    student_count=0  
    
    def __init__(self,name,age,surname):
      self.name=name
      self.age=age
      self.surname=surname
      Student.student_count+=1   #it will increment the student_count variable by 1 every time an object of the class is created, it is used to keep track of the number of students created.We can also use self.student_count+=1 but it will create a new instance variable student_count for each object of the class, it will not increment the class variable student_count, it will only increment the instance variable student_count for each object of the class.
      
      
student1=Student('Saheli', 19, 'Mondal')
student2=Student('Tomojit', 20, 'Bhattacharjee')
student3=Student('Tom', 20, 'Bhattacharjee')
print(student1.name, student1.age)
print(Student.session)
print(Student.student_count)
