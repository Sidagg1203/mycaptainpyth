import csv
def write_into_csv(info_list):
    with open('student_info.csv','a', newline=' ') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact number","Email id"])
        writer.writerow(info_list)

condition = True

while( condition):
    student_info = input('Enter the students information in the following format (Name age contact_number email_id)')

    student_info_list = student_info.split(' ')
    print("\nEntered infornmation of stundent is: \nName:{} \n Age:{} \nContact number:{} \nE mail:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    check = input("Is entered infornmation correct?(yes/no)")

    if check == 'yes':
        write_into_csv(student_info_list)
        condition_check = input("Do you want to enter another students infornmation?(yes/no)")
        if condition_check == "yes":
            condition = True
        elif condition_check == "no":
            condition = False
    elif check == "no":
        print ("Please enter the infornmation again")

