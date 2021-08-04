import json

def read_from_file():
    try:

        file = open("student.json", "r")
        file_content_as_text = file.read()
        students = json.loads(file_content_as_text)
        file.close()
        return students
    except :
        return []

def write_to_file(student):
    file = open("students.json", "w+")
    json_text = json.dumps(student,indent=6)
    file.writelines(json_text)
    file.close()

def add_contact():
    new_student = dict()
    new_student['first_name'] = word_both_cap((str(input("Enter First Name :  "))).strip())
    new_student['last_name']= word_both_cap((str(input("Enter Last Name :  "))).strip())
    new_student['id']= (str(input("Enter ID :  "))).strip()
    found_ = check_id(new_student['id'])
    if found_==0:
        print(end="")
    else:
        while True:
            new_student['id'] = (str(input("Already Have ! Enter ID Again ! :  "))).strip()
            found_ = check_id(new_student['id'])
            if  found_==0:
                break

    course_list = []

    p=int(input("How Many Course ? "))
    for i in range(p):
        p=input("Enter Course Code :  ")
        if p in course_list:
            print("Already Have ! Input Again !")
            p = input("Enter Course Code :  ")
            while True:
                if p in course_list:
                    print("Already Have ! Input Again !")
                    p = input("Enter Course Code")
                else:
                    break
        course_list.append(p)
    new_student['section'] = input("Enter Section Name :  ").strip()


    new_student['course_list'] = course_list

    new_student['reg_status'] = "Pending"

    students_array = read_from_file()

    students_array.append(new_student)

    write_to_file(students_array)
    print("-------------------------*****-------------------------")
    print("|                  Add Successfully !                 |")
    print("-------------------------*****-------------------------")

def check_id(verify_id):
    students_array = read_from_file()
    found_id= 0
    for student in students_array:
        if student.get("id") == verify_id:
            return 1
    return found_id

def search_student( id ):


    students_array = read_from_file()
    found__id= False
    for student in students_array:


        if student.get("id") == id:
            print()
            print("Name : " + student.get("first_name") + " " + student.get("last_name"))
            print("ID : ", student.get("id"))
            print("Course List : ")
            j = 1
            for i in student.get("course_list"):
                print("\t", j, end="." + " " + i + "\n")
                j += 1
            print("Section : ", student.get("section"))
            print("Registration Status : ", student.get("reg_status"),"\n")
            return True

    return found__id

def update_reg_status():

    update_id = (str(input("Enter ID :  "))).strip()
    students_array = read_from_file()
    new_data = []
    f = False
    for student in students_array:

        if student.get("id") == update_id:
            f = True
            print("Name : " + student.get("first_name") + " " + student.get("last_name"))
            print("ID : ", student.get("id"))
            print("Course List : ")
            j = 1
            for i in student.get("course_list"):
                print("\t", j, end="." + " " + i + "\n")
                j += 1
            print("Section : ", student.get("section"))
            print("Registration Status : ", student.get("reg_status"))

            if student.get("reg_status") == "Complete":
                print("Already Complete!\n")

            print("Choice Option : ")
            print("1. Pending")
            print("2. Partially Complete")
            print("3. Complete")
            print("4. Don't Want Change")
            i = int(input())
            if i == 1:
                student['reg_status']="Pending"
                print("Update Successfully !")
            elif i == 2 :
                student['reg_status'] = "Partially Complete"
                print("Update Successfully !")
            elif i == 3 :
                student['reg_status'] = "Complete"
                print("Update Successfully !")
            elif i == 4:
                print("Not Change")
            else:
                print("Wrong Key !")
            new_data.append(student)
        else:
            new_data.append(student)
    if not f :
        print("Data Not Found !\n")
    else:
        write_to_file(new_data)

def delete_student(del_id):
    c_a = read_from_file()#read file
    new_data = [] #create list
    check = False
    for entry in c_a:
        if del_id == entry.get("id"):
            check = True
            pass
        else:
            new_data.append(entry)#data add
    write_to_file(new_data)#write to json file
    return check

def view_record(): #print all  data
    students_array = read_from_file()
    count=1
    print("-------------------------*****-------------------------")
    for student in students_array:
        print(count,end=".\n")
        print("Name : "+student.get("first_name")+" "+student.get("last_name"))
        print("ID : ",student.get("id"))
        print("Course List : ")
        j=1
        for i in student.get("course_list"):
            print("\t",j,end="."+" "+i+"\n")
            j+=1
        print("Section : ", student.get("section"))
        print( "Registration Status : ",student.get("reg_status"))
        print()
        count+=1
    print("-------------------------*****-------------------------")

def statistics():
    pending_student=0
    complete_student=0
    partially_complete_student=0
    total_student=0
    students_array = read_from_file()
    for student in students_array:
        if student.get("reg_status")=="Pending":
            pending_student += 1
        elif student.get("reg_status")=="Partially Complete":
            partially_complete_student += 1
        elif student.get("reg_status")=="Complete":
            complete_student += 1
    total_student = pending_student+complete_student+partially_complete_student
    print(">>>  Total Student :  ",total_student)
    print(">>>  Registration Pending Student :  ", pending_student)
    print(">>>  Partially Complete Student : ",partially_complete_student)
    print(">>>  Registration Complete Student :  ", complete_student,"\n")


def edit_record():
    id = (str(input("Enter ID :  "))).strip()
    students_array = read_from_file()
    new_data = []
    f = False
    opinion=2
    for student in students_array:

        if student.get("id") == id:
            f = True

            print("First Name : " + student.get("first_name"))
            opinion=int(input("Want to Edit First Name ? 1.Yes 2.No  "))
            if opinion == 1:
                student['first_name'] = word_both_cap((str(input("Enter First Name :  "))).strip())

            print("Last Name : " + student.get("last_name"))
            opinion = int(input("Want to Edit Last Name ? 1.Yes 2.No  "))
            if opinion == 1:
                student['last_name'] = word_both_cap((str(input("Enter Last Name :  "))).strip())

            print("Id : " + student.get("id"))
            opinion = int(input("Want to Edit Id ? 1.Yes 2.No  "))
            if opinion == 1:
                found = int(check_id((str(input("Enter ID :  "))).strip()))
                if  found==0:
                    print(end="")
                else:
                    while True:
                        id = (str(input("Already Have ! Enter ID Again ! :  "))).strip()
                        found = int(check_id(id))
                        if found == 0:
                            break
                student['id'] = id
            print("Course List : ")
            j = 1
            for i in student.get("course_list"):
                print("\t", j, end="." + " " + i + "\n")
                j += 1
            course_list = []
            c_l=[]
            opinion = int(input("Want to Edit Id ? 1.Yes 2.No  "))
            if opinion == 1:
                for i in student.get("course_list"):
                    print(i)
                    opinion = int(input("Want Edit this ?  1. Yes 2.No  "))
                    p = input("Enter Course Code :  ")
                    if p in course_list:
                        print("Already Have ! Input Again !")
                        p = input("Enter Course Code :  ")
                        while True:
                            if p in course_list:
                                print("Already Have ! Input Again !")
                                opinion = int(input("Want Edit this ?  1. Yes 2.No "))
                                if opinion ==1:
                                    print("Already Have ! Input Again !")
                                    p = input("Enter Course Code")
                            else:
                                break
                    course_list.append(p)

            print("Section : ", student.get("section"))
            opinion = int(input("Want to Edit Section Name ? 1.Yes 2.No  "))
            if opinion == 1:
                section = input("Enter Section Name :  ")
                student['section'] = section
            print("Registration Status : ", student.get("reg_status"))
            opinion = int(input("Want to Edit Registration Status ? 1.Yes 2.No  "))
            if opinion == 1:

                print("Choice Option : ")
                print("1. Pending")
                print("2. partially complete")
                print("3. Complete")
                print("4. Don't Want Change")
                i = int(input())
                if i == 1:
                    student['reg_status'] = "Pending"
                    print("Update Successfully !")
                elif i == 2:
                    student['reg_status'] = "partially complete"
                    print("Update Successfully !")
                elif i == 3:
                    student['reg_status'] = "Complete"
                    print("Update Successfully !")
                elif i == 4:
                    print("Not Change")
                else:
                    print("Wrong Key !")


            new_data.append(student)
        else:
            new_data.append(student)
    if not f:
        print("Data Not Found !")
    else:
        write_to_file(new_data)


def word_both_cap(str):

    return ' '.join(map(lambda str: str[:-1] + str[-1],str.title().split()))

while True:
    print("-------------------------*****-------------------------")
    print("|                 1. New Registration                 |")
    print("|                 2. Search By ID                     |")
    print("|                 3. Update Registration Status       |")
    print("|                 4. Edit Record                      |")
    print("|                 5. Delete Record                    |")
    print("|                 6. View Record                      |")
    print("|                 7. Account                          |")
    print("|                 8. Exit                             |")
    print("-------------------------*****-------------------------")
    choice = int(input())

    if choice == 1:
        add_contact()

    elif choice ==2:
        search_id = (str(input("Enter ID :  "))).strip()
        found = search_student( search_id )
        if not found:
            print("-------------------------*****-------------------------")
            print("|                 Student Not Found !                 |")
            print("-------------------------*****-------------------------")

    elif choice == 3:
        update_reg_status()
    elif choice == 4:
        edit_record()
    elif choice == 5:

        found = delete_student((str(input("Enter ID :  "))).strip())
        if not found:
            print("-------------------------*****-------------------------")
            print("|                 Student Not Found !                 |")
            print("-------------------------*****-------------------------")
        else:
            print("-------------------------*****-------------------------")
            print("|                  Delete Successfully !              |")
            print("-------------------------*****-------------------------")
    elif choice == 6:
        view_record()

    elif choice == 7:
        statistics()

    elif choice == 8:
        exit()