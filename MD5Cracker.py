import hashlib
import time

x = 1

password_hash = input("Enter A  MD5 Hash\n>")

file = input("\nInsert The File Name\n>")

try:
    file = open(file, "r", encoding="ISO-8859-1")
except:
    print("\nThe File You Entered Is Invalid.")
    quit_ = input("\nPress ENTER To Quit.\n")
    quit()
        
for password in file:
    filemd5 = hashlib.md5(bytes(password.strip(), "ISO-8859-1")).hexdigest() 
    print("{:,}".format(x), "-", password.strip())
    x += 1
    if password_hash==filemd5:
        print("""\nMatch Found:
.
.
.
.\n""")
        print("Hash", filemd5 + ":", password)
        break

else:
    print("""\nNo Match Found:
.
.
.
.\n
Your Hash Was Not In The File.""")


time.sleep(120)
quit()
