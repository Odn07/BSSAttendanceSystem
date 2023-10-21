Additional functionality

Anytime a user signs in or out there is a greeting message that is displayed. i want to add a function that will grab the name of that user from the personal data file and print it out along with the greeting message.



STAFF ATTENDANCE MANAGEMENT SYSTEM

NOTE: IN PLACE OF USERNAME THE PROGRAM CAN BE UPGRADED TO USE INPUT DEVICE LIKE BARCODE READER 
THAT CAN READ BAR CODE FROM AN ID CARD OR A FINGER PRINT READER OR A FACE RECOGNITION TECHNOLOGY.

MENU:
1. ACCOUNT 
2. REGISTER
3. VIEW
4. SAVE
5. PRINT
6. DELETE

ABOUT STAFF ATTENDACE SYSTEM

1. The program will record staff attendance, the date and time they came to work and when they 
leave work

2. Each new staff will be registered and their personal information like name, job role, date
registered will be entered into a database.

3. The program will create new staff attendance record every month.

4. At the beginning of every work day, staff will enter their username/password. Once this is done 
the  date, name, job role, time-in and time-out, sign-in and sign-out will be entered into a database.

5. staff will be required to enter their username/password twice daily. When they come to work and 
when they leave. For this program to work, there will be a function that will have access to the 
username/password created in the staff personal record. If the username/password is present, 
then go ahead and process staff.  

6. The program will use username as a condition to either sign-in a staff or sign them out. so, if 
the username is in record sign-in/sign-out staff. 

THE CODE WILL LOOK LIKE THIS:

if username/password in employee personal file:         
            sign-in employee
        else:
            sign-out employee
else:
    ask user to create username/password.
    
            
7. At the beginning of every month a new attendance record will be created. To accomplish this 
the program need to be able to identify the first day of every month and then use it to create a
new attendance file.

8. In the access attendance menu function, names of previous attendance file will be displayed so 
the user can pick the file they want to access. To do this the program needs a function that can 
store names of attendance file created and read them.

9. Only admin will have access to files to view, delete and print

10. The program will create and store admin access information. With the aid of a condition if it 
matches then a access will be granted.



