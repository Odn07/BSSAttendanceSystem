import datetime, os.path, os, glob, csv
from datetime import date
from datetime import datetime, timedelta
from xlsxwriter.workbook import Workbook


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
    @classmethod
    def create_admin_signin_credentials(cls):
        print("\nCREATE ADMIN SIGN IN CREDENTIALS: \n")
        admin_credentials = cls.admin_signin_credentials()
        try:
            with open("admin-credentials.csv", "a", newline="") as file:
                fieldnames = ["username", "password"]
                writer = csv.DictWriter(file, fieldnames = fieldnames)
                #If file does not exist create header.            
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow({"username": admin_credentials.admin_username, "password": admin_credentials.admin_password})
                print("Admin account Created!")
        except BaseException:
            pass


class Employee:

    # registers new staff, only admin authorised to do this,
    #  require admin sign in credentials
    @classmethod
    def create_employee_data(cls):
        print("\nREGISTER STAFF: \n")
        credentials = []
        try:
            with open("admin-credentials.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    credentials.append(row)
        except BaseException:
            pass

        admin_credentials = Admin.admin_signin_credentials()
        for cred in credentials:    
            if admin_credentials.admin_username == cred["username"] and admin_credentials.admin_password == cred["password"]:
                try:
                    # create and hold new employee record   
                    username = input("Staff unique username: ")
                    name = input("Staff name: ").title()
                    department = input("Department: ").title()
                    job = input("Job role: ").title()
                except BaseException:
                    pass
                try:
                    with open("employee-file.csv", "a", newline="") as file:
                        fieldnames = ["date", "username", "name", "department", "job"]
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        #If file does not exist create header.            
                        if file.tell() == 0:
                            writer.writeheader()
                        writer.writerow({"date": date.today(), "username": username, "name": name, "department": department, "job": job})
                except BaseException:
                    print("Can't write to employee file!")
            else:
                print("Access denied!")




    @classmethod
    def get_employee_name(cls, user_name):
        with open("employee-file.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if user_name == row["username"]:
                    return row["name"]



class Temp:
    # delete old temp file
    @classmethod    
    def delete_previous_month_csv_file(cls):
        if(os.path.exists(cls.locate_previous_month_csv_file()) and os.path.isfile(cls.locate_previous_month_csv_file())):
            os.remove(cls.locate_previous_month_csv_file()) 
        


    # identify old temp file  
    @classmethod  
    def locate_previous_month_csv_file(cls):   
        current_date = date.today() - timedelta(51)
        old_temp_file_name = date(current_date.year, current_date.month, current_date.day)
        ext = "monthly_file.csv"
        return f"{str(old_temp_file_name) + ext}"


    # delete old temp file
    @classmethod
    def delete_temp_file(cls):
        if(os.path.exists(cls.old_temp_file()) and os.path.isfile(cls.old_temp_file())):
            os.remove(cls.old_temp_file()) 

    # identify old temp file
    @classmethod
    def old_temp_file(cls):   
        current_date = date.today() - timedelta(1)
        old_temp_file_name = date(current_date.year, current_date.month, current_date.day)
        ext = "T.csv"
        return f"{str(old_temp_file_name) + ext}"

    # create a daily temporary file
    @classmethod
    def temp_file(cls):
        current_date = date.today()
        daily_file_name = date(current_date.year, current_date.month, current_date.day)
        ext = "T.csv"
        return f"{str(daily_file_name) + ext}" 



    # a daily file that temporarily stores sign-in/sign-out activities, the file
    #  is deleted at the beginning of the next working day.
    @classmethod   
    def create_temp_file(cls, username):
        # delete old temp file
        cls.delete_temp_file()    
        #read employee file to employee list
        employee_list = []
        try:
            with open("employee-file.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employee_list.append(row)
        except BaseException:
            print("Can't read employee file!")     

        # loop thru employee list
        for employee in employee_list:
            if username == employee["username"]:    
                name = employee["name"]
                department = employee["department"]
                job = employee["job"] 

                try:
                    with open(cls.temp_file(), "a", newline="") as file:
                        fieldnames = ["date", "username", "name", "department", "job", "time"]
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        #If file does not exist create header.            
                        if file.tell() == 0:
                            writer.writeheader()
                        writer.writerow({"date": date.today(), "username": username, "name": name, "department": department, "job": job})                    
                except BaseException:
                    print("Can't write to temp file!")   
        # check if staff is signed in/out
        Attendance.check_attendance_status(username)





class Attendance:

    # check the temp file if staff has signed in/out for the day, display a 
    # message to alert staff
    @classmethod
    def check_attendance_status(cls, username):
        currentT = datetime.now().strftime("%H:%M:%S")
        attendance_count = []
        with open(Temp.temp_file()) as file:
            reader = csv.DictReader(file)
            for row in reader:  
                attendance_count.append(row["username"]) 
            attendance = attendance_count.count(username)        
            if attendance == 1:
                print(f"Successful! You Signed-In @{currentT}. Welcome {Employee.get_employee_name(username)}!")
            elif attendance ==2:
                print(f"Successful! You Signed-Out @{currentT}. Goodbye {Employee.get_employee_name(username)}!")
            else:
                print(f"Try again tomorrow {Employee.get_employee_name(username)}!") 

    
    
    @classmethod
    def attendance_status(cls, username):
        attendance_count = []
        with open(Temp.temp_file()) as file:
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
    


    # a monthly file that stores daily sign-in/sign-out activities
    @classmethod
    def create_attendance(cls, username): 
        Temp.delete_previous_month_csv_file()              
        day = date.today().strftime("%A")
        #read employee file to employee list
        employee_list = []
        try:
            with open("employee-file.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employee_list.append(row)
        except BaseException:
            print("Can't read employee file!")     
        
        # loop thru employee list
        for employee in employee_list:
            if username == employee["username"]:    
                name = employee["name"]
                department = employee["department"]
                job = employee["job"]                
        try:                    
            with open(cls.attendance_file_name(), "a", newline="") as file:        
                fieldnames = ["day", "date", "username", "name", "department", "job", "time", "status"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                #If file does not exist create header.            
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow({"day": day, "date": date.today(), "username": username, "name": name, "department": department, "job": job, "time": datetime.now().strftime("%H:%M:%S"), "status": cls.attendance_status(username)})
        except BaseException:
            pass
                        
                

    '''
    THIS FUNCTION WILL CREATE NEW ATTENDANCE FILE EVERY MONTH
    '''
    @classmethod
    def attendance_file_name(cls):       
        current_date = date.today()
        first_day_of_month = date(current_date.year, current_date.month, 1)
        ext = "monthly_file.csv"    
        attendance_filename = f"{str(first_day_of_month) + ext}"            
        return attendance_filename


    @classmethod
    def process_attendance(cls):
        currentT = datetime.now().strftime("%H:%M:%S")
        current_date = date.today()
        date_today = date(current_date.year, current_date.month, current_date.day)
        print("DATE:", current_date.strftime("%A"), ",", date_today, "\nTIME:", currentT)

        print("\nSIGN-IN OR SIGN-OUT WITH YOUR USERNAME\n")

        '''
        CREATE ATTENDANCE
        '''

        while True:
            try:            
                username = input("PRESS ENTER KEY AFTER ENTERING YOUR USERNAME HERE: ").strip()
                         
                if username == "admin":
                    break
                    
                elif username:
                    
                    # a daily file that temporarily stores sign-in/sign-out activities, the file is deleted at the beginning
                    #of the next working day.                
                    Temp.create_temp_file(username) 
                    print("\n")
                    # a monthly file that stores daily sign-in/sign-out activities                   
                    cls.create_attendance(username)
                    #Converts monthly csv file to excel file.
                    cls.csv_to_excel()
                                
                                                                
                else:
                    # otherwise access is denied. And employee need to check the username they entered or create
                    # a new username if they are newly employed
                    print("Access denied! Check username.")                               
            except:
                print("Unknown username!")
    
    
    
    @classmethod    
    def csv_to_excel(cls):        
        for csvfile in glob.glob(os.path.join(".", "*monthly_file.csv")):
            workbook = Workbook(csvfile[:-4] + '.xlsx')
            worksheet = workbook.add_worksheet()
            with open(csvfile, 'rt', encoding='utf8') as f:
                reader = csv.reader(f)
                for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        worksheet.write(r, c, col)
            workbook.close()    



def main():
    counter = 0
    

if __name__ == "__main__":
    main()

"""
create a function that displays old attendance file name.
create a function that allow admin to have access to records.
"""            
    
