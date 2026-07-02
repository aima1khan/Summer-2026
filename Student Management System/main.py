from student import Student

students = []
choice=0
while choice!=7:
    print("=====Student Management System=====")
    print("1.Add Student \n2.Search Student \n3.View Students \n4.Delete Student \n5.Add Subject \n6.Add Grade \n7.Exit")
    choice=int(input("Enter Choice :"))
    if choice==1:
        name=input("Enter Name :")
        age=int(input("Enter Age :"))
        roll_no=int(input("Enter Roll Number :"))
        field_of_study=input("Enter Field Of Study :")
        student=Student(name,age,roll_no,field_of_study)
        students.append(student)
        print("Student Added Successfully!")
        

    elif choice==2:
        roll_no=int(input("Enter Student Roll Number :"))
        found=False
        for student in students:
            if roll_no == student.roll_no:
                found=True
                student.display_info()            
                break
        if not found:
            print("Student Not Found!")

    elif choice==3:
        if not students:
            print("No Student Found")
        else:
            print("====Displaying Student====")
            for student in students:
                student.display_info()

    elif choice==4:
        roll_no=int(input("Enter Student Roll Number :"))
        found=False
        for student in students:
            if roll_no == student.roll_no:
                found=True
                students.remove(student)
                print("Student Deleted Successfully!")            
                break
        if not found:
            print("Student Not Found!")

    elif choice==5:
        roll_no=int(input("Enter Student Roll Number :"))
        found=False
        for student in students:
            if roll_no == student.roll_no:
                found=True
                n = int(input("How many subjects do you want to add? "))
                for i in range(n):
                    subject = input(f"Enter subject {i+1}: ")
                    student.subjects.append(subject)
                print("Subjects added successfully!")
                break
        if not found:
            print("Student Not Found!")

    elif choice == 6:
        roll_no = int(input("Enter Student Roll Number : "))
        found = False
        for student in students:
            if roll_no == student.roll_no:
                found = True
                subject = input("Enter Subject Name: ")
                grade = input("Enter Grade: ")
                student.grades[subject] = grade
                print("Grade added successfully!")
                break

        if not found:
            print("Student Not Found!")
    elif choice == 7:
        print("Exiting System... Goodbye!")
        break
    
    else:
        print("Invalid Input!")