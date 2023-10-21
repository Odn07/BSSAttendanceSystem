from mod import *

def view_staff_attendance():
    #display list of stored file names for admin to easily make a choice
    open_attendance_filename_file2()
    file_input= input("Enter the staff attendance file name you wish to view: ")
    ext = ".csv"
    staff_attendance_filename = f"{file_input + ext}"
    counter = 0
    cprint(f"\nSTAFF ATTENDANCE FOR {file_input} \n", "yellow")

    with open(staff_attendance_filename) as file:
        reader = csv.DictReader(file)
        attendance_list = [row for row in reader]
        
        for attendance in attendance_list:
            counter += 1
            print(counter, " ", attendance["day"], attendance["date"], " ", attendance["name"], " ", attendance["department"], " ", attendance["job"], " ", attendance["time"], " ", attendance["status"])
            print("\n")


view_staff_attendance()
