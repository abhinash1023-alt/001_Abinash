#List: are used to store the multiple values in the single variable

a=["Rachit", "Vaishnavi", 'Shalini',12]
print(type(a))

#Tuples: are used to store the multiple values in the single variable but tuples are immutable

















# i=7
# while i < 10:
# i+=1
# printf(i)

count=[]

while count >0:
    if count %2 == 0:
        print(f"{count} is even")
    else:
        print(f"{count}is odd")
        count-=1


        #For Loop :

        nums=[1,2,3,4,5,6,7,8,9]

        for num in nums:
            if num%2 ==0:
                print(f"{num} is even")
            else:
                print(f"{num} is odd")

            for i in range(1,11,2):
                print(i)



#Create a code for student Grades
#inside array multiple students marks store
#Acoording to their particular number marks will be decided 
#Hint : Use For loop and If else.
a=(62,75,83,23,45,55,35,88,92,100)

students_marks = {"Rachit": 62, "Vaishnavi": 75, "Shalini": 83, "Amit": 23, "Neha": 45, "Rahul": 55, "Priya": 35, "Ankit": 88}
 for student, marks in students_marks.items():
    if marks >= 90:
        grade = 'A+'
elif marks >= 80:
grade = 'A'
elif marks >= 70:
grade = 'B+'
elif marks >= 60:
grade = 'B'
elif marks >= 50:
grade = 'C'
else:
    grade = 'F'
print(f"{student} scored {marks} and grade {grade}.")
print("hello world")

             