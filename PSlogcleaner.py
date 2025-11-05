import os

print("*** This tool is designed by 'https://github.com/spiritofthenight' for automating deleting Powershell logs in windows ! ***\n")

def PowerSmoke() :
    ppath = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "PowerShell", "PSReadLine") # for windows 10 and 11

    os.chdir(ppath)

    for file in os.listdir():
        os.remove(file)
    print("Hell yea ! all Powershell logs are gone for good!\n")

def main():
    while True:
        try:
            command = int(input("please enter 0 if you want to clearout your powershell logs ! or enter 1 to exit .\n"))
            if command == 0:
                PowerSmoke()
                break
            elif command == 1:
                print("you have exited the app !\n")
                exit()
            else:
                print("wrong command !\n")
        except ValueError:
            print("only enter 0 or 1\n0 = delete Powershell logs\n1 = exit the app\n")

if __name__ == "__main__":
    main()