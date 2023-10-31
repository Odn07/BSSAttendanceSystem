import mod

'''
STAFF ATTENDANCE MANAGEMENT SYSTEM
'''

print("\nATTENDANCE SYSTEM\n")
print("MENU =>: |ACCOUNT, |REGISTER")


print("\n")
mod.Attendance.process_attendance()


while True:
    try:
        menu = input("Enter menu: ").title()
        if not menu:
            break
        menu_list = ["Account", "Register"]
        if menu in menu_list:
            match menu:
                case "Account":
                    mod.Admin.create_admin_signin_credentials()
                case "Register":
                    mod.Employee.create_employee_data()                
                case _:
                    pass
                

    except:
        print("Wrong input!")


#WORK IN PROGRESS ....        
