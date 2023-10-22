from mod import *

# delete old temp file    
def delete_previous_monthly_file():
    if(os.path.exists(locate_previous_monthly_file()) and os.path.isfile(locate_previous_monthly_file())):
        os.remove(locate_previous_monthly_file()) 
    print("file is deleted")


# identify old temp file    
def locate_previous_monthly_file():   
    current_date = date.today() - timedelta(51)
    old_temp_file_name = date(current_date.year, current_date.month, current_date.day)
    ext = "monthly_file.csv"
    print(f"{str(old_temp_file_name) + ext}")

locate_previous_monthly_file()