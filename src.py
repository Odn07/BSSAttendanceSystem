import mod

'''
STAFF ATTENDANCE MANAGEMENT SYSTEM
'''

print("\nATTENDANCE SYSTEM\n")
print("MENU =>: |Account, |Register\n")

menu = int(input("PRESS 1 TO SIGN-IN/SIGN-OUT, 2 TO USE MENU, ZERO TO LOGOFF. "))

match menu:
    case 1:
        print("\n")
        mod.Attendance.process_attendance()
    case 2:
        while True:
            try:
                menu = input("Menu: ").title()
                if menu == "Admin":
                    break
                menu_list = ["Account", "Register"]
                if menu in menu_list:
                    match menu:
                        case "Account":
                            mod.Admin.create_admin_signin_credentials()
                        case "Register":
                            mod.Employee.create_employee_data()            
                                        
                        case _:
                            print("Invalid input")
                            
            except:
                print("Wrong input!")

    case 0:
       pass


#mod.Admin.create_admin_signin_credentials()



#WORK IN PROGRESS ....        
