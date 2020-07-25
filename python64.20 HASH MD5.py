import hashlib
import time
#Latin-1, not UTF-8
x = 1

password_hash = input("Enter A  MD5 (128bit) Hash\n>")
#while len(password_hash) != 32:
 #   password_hash = input("\nInvalid Entry: Length Not Valid. Try Again.\n>")
file = input("\nInsert The File Name (SPACE For Default)\n>")
if file.upper() == " ":
    file = (r"C:\Users\John\Downloads\TXTV7.txt")

try:
    file = open(file , "r" , encoding = "ISO-8859-1")
except:
    print("\nThe File You Entered Is Invalid.")
    quit_ = input("\nPress ENTER To Quit.\n")
    if quit_ == " ":
        quit()
    else:
        quit()
        
for password in file:
    filemd5 = hashlib.md5(bytes(password.strip() , "ISO-8859-1")).hexdigest() 
    #print(filemd5)
    print("{:,}".format(x) , "-" , password.strip())
    x += 1
    if password_hash == filemd5:
        print("""\nMatch Found:
.
.
.
.\n""")
        print("Hash" , filemd5 + ":" , password)
        break
    #if x == 30:
       #break
else:
    print("""\nNo Match Found:
.
.
.
.\n
Your Hash Was Not In The Index.""")


time.sleep(120)
quit()
