name = "hariAddsDSSS"
no = "6374198604"
aadhaar_no = "5678 8930 9744"

print(name.lower())

print(name.upper())

print(name.capitalize())

print(name[2:])
print(name[:-4])
print(no[:2]+"********"+no[-2:])
print(aadhaar_no[:5]+"****"+aadhaar_no[-5:])
print(f"my name is {name}.my mobile number is {no}")

song  = "singam Singam"
artist = "HARI haran"
print(f"{song.title()} - {artist.title()}")

location = "omalur,salem-636309"
fixed_location = location.replace("omalur","kamalapuram")
print(location)
print(fixed_location)

message = "your uid is : hari1234@. your password is : harihari2004"
password = message.split("password")[1].split(":")[1].split(".")[0].strip()
print(password)

college = "student reg no : 720722115025.\nmy name is hariharan k,he is great man.\nhello "
print(college)
reg_no = str(input("enter the reg no:"))
if reg_no in college:
    print("yes")
    print(reg_no)
else:
    print("no")
print(college.find(reg_no))    

current_name = str(input("Enter the names:"))
initials = ([word[0].upper() for word in current_name.split()])
print(current_name)
print(initials)

category = "chicken mutton seafoods oceanfoods"
initial = " ".join([word[-1].upper() for word in category.split()])
print(initial)

game = "   sivadharshini   "
print(game.strip().upper())

word1 = "my girl so cute and looks like pretty"
word_count = len(word1.split())
print(word_count)

