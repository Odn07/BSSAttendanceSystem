import csv
import datetime, os.path
from datetime import date
from datetime import datetime, timedelta
from termcolor import *
import colorama
colorama.init()

def main():
    counter = 0
'''
1. write a code to stop any other account creation after the first one has been created.
2. for any other account to be created the first one must grant permission.
3. write a code to generate admin password and username in case they forget them.
'''





class Admin:
    def __init__(self, admin_username, admin_password):
        self.admin_username = admin_username
        self.admin_password = admin_password

    def __str__(self):
        return f"{self.admin_username}, {self.admin_password}"
    
    @property
    def admin_usernames(self):
        return self.admin_username
        
    
    @admin_usernames.setter
    def admin_usernames(self, admin_username):
        if not admin_username:
            raise ValueError("Missing username!")
        self.admin_username = admin_username

    @property
    def admin_passwords(self):
        return self.admin_password
    
        

    @admin_passwords.setter
    def admin_passwords(self, admin_password):
        if not admin_password:
            raise ValueError("Missing password!")
        self.admin_password = admin_password    

    
    @classmethod
    def admin_signin_credentials(cls):
        admin_username = input("Admin Username: ")
        admin_password = input("Admin Password: ")
        try:
            return cls(admin_username, admin_password)
        except ValueError:
            print("Invalid input!")


# create and stores admin sign in credentials
def create_admin_signin_credentials():
    cprint("\nCREATE ADMIN SIGN IN CREDENTIALS: \n", "green")
    admin_credentials = Admin.admin_signin_credentials()
    try:
        with open("admin-credentials.csv", "a") as file:
            fieldnames = ["username", "password"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            #If file does not exist create header.            
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({"username": admin_credentials.admin_username, "password": admin_credentials.admin_password})
    except FileNotFoundError:
        pass
    except BaseException:
        pass


# registers new staff, only admin authorised to do this, require admin sign in credentials
def create_staff_data():
    cprint("\nREGISTER STAFF: \n", "green")
    credentials = []
    try:
        with open("admin-credentials.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                credentials.append(row)
    except FileNotFoundError:
        pass

    admin_credentials = Admin.admin_signin_credentials()
    for cred in credentials:    
        if admin_credentials.admin_username != cred["username"] or admin_credentials.admin_password != cred["password"]:
            print("Access denied! You're not an admin!!")
        elif admin_credentials.admin_username == cred["username"] and admin_credentials.admin_password == cred["password"]:
            # create and hold new employee record   
            username = input("Staff unique username: ")
            name = input("Staff name: ").title()
            department = input("Department: ").title()
            job = input("Job role: ").title()
            try:
                with open("employee-file.csv", "a") as file:
                    fieldnames = ["date", "username", "name", "department", "job"]
                    writer = csv.DictWriter(file, fieldnames = fieldnames)
                    #If file does not exist create header.            
                    if file.tell() == 0:
                        writer.writeheader()
                    writer.writerow({"date": date.today(), "username": username, "name": name, "department": department, "job": job})
            except FileNotFoundError:
                print("Can't write to employee file!")


def delete_file():
    '''
    REQUIRE ADMINISTRATORS PASSWORD AND USERNAME TO DELETE FILE
    '''
    cprint("ENTER USERNAME AND PASSWORD TO DELETE FILE: ", "green")
    credentials = []
    try:
        with open("admin-credentials.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                credentials.append(row)
    except FileNotFoundError:
        pass

    admin_credentials = Admin.admin_signin_credentials()
    for cred in credentials:    
        if admin_credentials.admin_username != cred["username"] or admin_credentials.admin_password != cred["password"]:
            print("Access denied! You're not an admin!!")
        elif admin_credentials.admin_username == cred["username"] and admin_credentials.admin_password == cred["password"]:                
            # delete file
            '''
            TO DELETE ENTER THE NAME OF FILE TO DELETE        
            To delete a csv file
            first check if file exists
            call remove method to delete the csv file
            '''
            filename_to_delete = input("File to delete: ")
            ext = ".csv"
            file = f"{filename_to_delete + ext}"
            if(os.path.exists(file) and os.path.isfile(file)):
                os.remove(file) 
            cprint(f"{filename_to_delete} file is deleted!", "yellow") 



# delete old temp file
def delete_temp_file():
    if(os.path.exists(old_temp_file()) and os.path.isfile(old_temp_file())):
        os.remove(old_temp_file()) 



# identify old temp file
def old_temp_file():   
    current_date = date.today() - timedelta(31)
    old_temp_file_name = date(current_date.year, current_date.month, current_date.day)
    ext = "T.csv"
    return f"{str(old_temp_file_name) + ext}"

# create a daily temporary file
def temp_file():
    current_date = date.today()
    daily_file_name = date(current_date.year, current_date.month, current_date.day)
    ext = "T.csv"
    return f"{str(daily_file_name) + ext}" 

"""
Name of function: get_employee_name

Purpose: The get_employee_name()function will return the name of the employee whose username matches the corresponding username extracted from the file passed into the function as argument.
"""

def get_employee_name(user_name):
    with open("employee-file.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if user_name == row["username"]:
                return row["name"]



# check the temp file if staff has signed in/out for the day, display a message to alert staff
def check_attendance_status(username):
    currentT = datetime.now().strftime("%H:%M:%S")
    attendance_count = []
    with open(temp_file()) as file:
        reader = csv.DictReader(file)
        for row in reader:  
            attendance_count.append(row["username"]) 
        attendance = attendance_count.count(username)        
        if attendance == 1:
            print(f"Successful! You Signed-In @{currentT}. Welcome {get_employee_name(username)}!")
        elif attendance ==2:
            print(f"Successful! You Signed-Out @{currentT}. Goodbye {get_employee_name(username)}!")
        else:
            print(f"Try again tomorrow {get_employee_name(username)}!") 


def attendance_status(username):
    attendance_count = []
    with open(temp_file()) as file:
        reader = csv.DictReader(file)
        for row in reader:  
            attendance_count.append(row["username"]) 
        attendance = attendance_count.count(username)        
        if attendance == 1:
            return f"{'Signed-In'}"
        elif attendance ==2:
            return f"{'Signed-Out'}"
        else:
            return f"{'Invalid'}"   
    

# a daily file that temporarily stores sign-in/sign-out activities, the file is deleted at the beginning
#of the next working day.
def create_temp_file(username):
    # delete old temp file
    delete_temp_file()    
    #read employee file to employee list
    employee_list = []
    try:
        with open("employee-file.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employee_list.append(row)
    except FileNotFoundError:
        print("Can't read employee file!")     

    # loop thru employee list
    for employee in employee_list:
        if username == employee["username"]:    
            name = employee["name"]
            department = employee["department"]
            job = employee["job"] 

            try:
                with open(temp_file(), "a") as file:
                    fieldnames = ["date", "username", "name", "department", "job", "time"]
                    writer = csv.DictWriter(file, fieldnames = fieldnames)
                    #If file does not exist create header.            
                    if file.tell() == 0:
                        writer.writeheader()
                    writer.writerow({"date": date.today(), "username": username, "name": name, "department": department, "job": job})                    
            except FileNotFoundError:
                print("Can't write to temp file!")   
    # check if staff is signed in/out
    check_attendance_status(username)
    

# a monthly file that stores daily sign-in/sign-out activities
def create_staff_attendance(username):
    day = date.today().strftime("%A")
    #read employee file to employee list
    employee_list = []
    try:
        with open("employee-file.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employee_list.append(row)
    except FileNotFoundError:
        print("Can't read employee file!")     

    # loop thru employee list
    for employee in employee_list:
        if username == employee["username"]:    
            name = employee["name"]
            department = employee["department"]
            job = employee["job"] 

            try: 
                with open(attendance_file_name(), "a") as file:        
                    fieldnames = ["day", "date", "username", "name", "department", "job", "time", "status"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    #If file does not exist create header.            
                    if file.tell() == 0:
                        writer.writeheader()
                    writer.writerow({"day": day, "date": date.today(), "username": username, "name": name, "department": department, "job": job, "time": datetime.now().strftime("%H:%M:%S"), "status": attendance_status(username)})
            except FileNotFoundError:
                print("Can't write to attendance file!")
                break            
        else:
            pass

'''
THIS FUNCTION WILL CREATE NEW ATTENDANCE FILE EVERY MONTH
'''
def attendance_file_name():       
    current_date = date.today()
    first_day_of_month = date(current_date.year, current_date.month, 1)
    ext = ".csv"    
    attendance_filename = f"{str(first_day_of_month) + ext}"
    create_attendance_filename_file2(attendance_filename)
    create_attendance_filename_file1(attendance_filename)        
    return attendance_filename


# write the names of attendance filename created monthly into a file 
#attendance_filename_file() 
def create_attendance_filename_file1(file_name):     
    # write the names of attendance filename created monthly into a file    
    try:
        with open("attendance-file-name1.csv", "w") as file:
            fieldnames = ["file_name"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            #If file does not exist create header.            
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({"file_name": file_name})
    except FileNotFoundError:
        pass
    


def create_attendance_filename_file2(file_name):    
    counter = 0
    attendance_filenames1 = []
    try:
        with open("attendance-file-name1.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                file_name1 = row["file_name"]    
                if  file_name != file_name1:                                                    
                    attendance_filenames1.append(file_name) 

    except FileNotFoundError:
        pass
    for _ in attendance_filenames1:       
        counter += 1        
                      
        try:
            with open("attendance-file-name2.csv", "a") as file:
                fieldnames = ["counter", "date", "file_name"]
                writer = csv.DictWriter(file, fieldnames = fieldnames)
                #If file does not exist create header.            
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow({"counter": counter, "date": date.today(), "file_name": file_name})
        except FileNotFoundError:
            pass
        break
        


def open_attendance_filename_file2():    
    attendance_filenames2 = []
    attendance_filenames3 = []
    try:
        with open("attendance-file-name2.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                attendance_filenames2.append(row["file_name"]) 
                attendance_filenames3.append(row)               
    except FileNotFoundError:
        pass
    cprint("STAFF ATTENDANCE FILE NAME: ", "yellow")
    for attendance2 in attendance_filenames2:
        for attendance3 in attendance_filenames3:
            filename_minus_csv = attendance2[0:10]
        
    '''
    remove .csv from attendance_filename before writing into file
    attendance_file_name = attendance_filename - .csv
    '''
    print(attendance3["counter"], ",", attendance3["date"], ",", "FILE NAME: ", filename_minus_csv)


def view_staff_attendance():
    #display list of stored file names for admin to easily make a choice
    open_attendance_filename_file2()
    file_input= input("Enter the staff attendance file name you wish to view: ")
    ext = ".csv"
    staff_attendance_filename = f"{file_input + ext}"
    counter = 0
    cprint(f"\nSTAFF ATTENDANCE FOR {file_input} \n", "yellow")
    attendance_list = []
    with open(staff_attendance_filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            attendance_list.append(row)
    for attendance in attendance_list:
        counter += 1
        print(counter, "  ", attendance["day"], attendance["date"], "  ", attendance["name"], "  ", attendance["department"], "  ", attendance["job"], "  ", attendance["time"], "  ", attendance["status"])
    print("\n")
    input_response = input("Type 's' to save and 'p' to print staff attendance: ").title()
    if not input_response:
        pass
    elif input_response == "S":
        ...
    elif input_response == "P":
        ...


def process_attendance():
    currentT = datetime.now().strftime("%H:%M:%S")
    current_date = date.today()
    date_today = date(current_date.year, current_date.month, current_date.day)
    print("DATE:", current_date.strftime("%A"), ",", date_today, "\nTIME:", currentT)

    cprint("\nSIGN-IN OR SIGN-OUT WITH YOUR USERNAME\n", "green")

    '''
    CREATE ATTENDANCE
    '''

    while True:
        try:            
            username = input("ENSURE YOU PRESS THE ENTER KEY AFTER ENTERING YOUR USERNAME HERE: ")          
            if not username:
                break
                
            elif username:
                # a daily file that temporarily stores sign-in/sign-out activities, the file is deleted at the beginning
                #of the next working day.                
                create_temp_file(username) 
                print("\n")
                # a monthly file that stores daily sign-in/sign-out activities                   
                create_staff_attendance(username)
                               
                                                              
            else:
                # otherwise access is denied. And employee need to check the username they entered or create
                # a new username if they are newly employed
                print("Access denied! Check username.")                               
        except:
            print("Unknown username!")
    
    




if __name__ == "__main__":
    main()

"""
create a function that displays old attendance file name.
create a function that allow admin to have access to records.
"""            
    
