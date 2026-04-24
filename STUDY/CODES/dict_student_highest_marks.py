student={}
n=int(input('Enter the range'))
for i in range(n):
  S_name=input('Enter Student name : ')
  S_marks=int(input('Enter marks: '))
  student[S_name]=S_marks
print(student)
highest={}
max=0
for S_name in student:
  if student[S_name]>max:
    max=student[S_name]
for S_name in student:
  if student[S_name]==max:
    highest[S_name]=student[S_name]
print(highest)