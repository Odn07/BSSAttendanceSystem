from mod import *

'''
STAFF ATTENDANCE MANAGEMENT SYSTEM
'''

cprint("\nBRILLIANT STAR SCHOOLS STAFF ATTENDANCE SYSTEM\n", "green")
cprint("MENU =>: |ACCOUNT, |REGISTER, |VIEW, |EDIT", "yellow")


print("\n")
process_attendance()


while True:
    try:
        menu = input("Enter menu: ").title()
        if not menu:
            break
        menu_list = ["Account", "Register", "View", "Edit"]
        if menu in menu_list:
            match menu:
                case "Account":
                    create_admin_signin_credentials()
                case "Register":
                    create_staff_data()                
                case "View":
                    view_staff_attendance()
                case "Edit":
                    '''
                    At the end of the editing task, prompt user
                    to save, and then print file.
                    '''
                    ...                      
                case _:
                    ...
                

    except:
        print("Wrong input!")


#WORK IN PROGRESS ....        
