''' Name = str(input("enter the name:"))
Age  = int(input("enter the age:"))
Student = bool(input("yes or no:"))
if Age >= 60 or Student =='yes':
    print(Name+" is eligible for discount")
else:
    print(Name+" is not eligible for discount")
'''
'''
import sys
if len(sys.argv) == 2:
    print("Usage: python email_generated.py 'Full name and Last name'")
    sys.exit()
Full_name = sys.argv[1]
Last_name = sys.argv[2]
#format for mail
email = Full_name.lower().replace(" ",".")+Last_name + "@gmail.com"
#output
print("\n--- Your Profile ---")
print("Full Name:", Full_name+Last_name)
print("generated Email:",email)
'''


import sys
fullname = " ".join(sys.argv[1:])
email = fullname.lower().replace(" ",".")+"@gmail.com"

print("--your profile--")
print("fullname:",fullname)
print("Email:",email)