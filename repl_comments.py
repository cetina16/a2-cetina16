# Borrowed from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
from hashlib import sha256
def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

my_list=[]
num=1
i=0

password_hash = "c2e2de13717990810a222f960c2b73f7d981a7a230a8c5b05ea622ddcc6e1710"
pw1 = input("Enter your password:")
hsh1 = create_hash(pw1)


if hsh1==password_hash:
    print("login completed")

    while num==1:
        comments=input("Enter some comments:")
        my_list.append(comments)
        print("Previously entered comments:")

        for i in range (len(my_list)):
            print(int(i+1), ".", my_list[i])
            i=i+1
else:
    print("Login failed, enter the correct password!")