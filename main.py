# A simple program with simple login logic and file manipulation
# Creates a txt file "userdata" to use as database (stores passwords insecurely)
# Has two different user privileges
# Tested on Windows only 


from random import randint
from os import system
# from getpass import getpass # [input] for dumb terminals [getpass] for security

USERS = {}


# log in function, checks if the user exist, returning false or true
def login(user, passwd):
    readfile()
    if user in USERS:
        if USERS[user]["passwd"] == passwd:
            return True
        else:
            system("cls")
            print("-> Wrong password\n")
    else:
        system("cls")
        print("-> User not found\n")
        return False


# sign in function, checks if the user exist, if not, add a new user to the FILE (not the USERS dict)
def signin(user, passwd, role="common-user"):
    readfile()
    if user in USERS:
        system("cls")
        return False
    else:
        with open("userdata.txt", "a") as datafile:
            datafile.write(f"{user},{passwd},{role}\n")
        return True


# Check if the file "data.txt" exist.
# If not, create a file with a admin login
# If it exists, does nothing
def filestartup():
    try:
        with open("userdata.txt", "r"):
            pass
    except FileNotFoundError:
        with open("userdata.txt", "w") as datafile:
            datafile.write(f"admin,admin,super-user\n")


# Reads file "data.txt" and adds info to the dict USERS
def readfile():
    filestartup()
    with open("userdata.txt", "r") as datafile:
        lines = datafile.readlines()
        for line in lines:
            info = line.split(",")
            USERS[info[0]] = {
                "passwd": info[1],
                "role": info[2]}


# Translates the USERS dict to the userdata.txt file
def savefile():
    filestartup()
    with open("userdata.txt", "w") as datafile:
        for user in USERS:
            datafile.write(f"{user},{USERS[user]['passwd']},{USERS[user]['role']}")


# If the person type a non existent option, those messages randomly appear
def randommessages():
    messageNumber = randint(1, 5)
    match messageNumber:
        case 1:
            print("-> To select an option, you can type the number before it or write the content between []\n")
        case 2:
            print("-> Uh oh, you missed?\n")
        case 3:
            print("-> You can check where you are by looking at the top right corner text\n")
        case 4:
            print("-> You can just hit enter instead of typing Y to exit\n")
        case 5:
            print("-> Did you know there is a hidden menu?\n")


def adminmenu(user):
    while True:
        readfile()
        print("=-=          -           =-=     -> Admin Menu")
        print("1 - [Add] user")
        print("2 - [Show] users")
        print("3 - [Remove] user")
        print("0 - [Exit]")
        print("=-=          -           =-=")
        option = input(": ").lower()
        match option:
            # Adds a new user same as signin function, but this one asks for user role (super or commom)
            case "add" | "1":
                system("cls")

                print("-=          -           =-=      -> Admin sing up")
                signInUser = input("Type your username: ")
                passwd = input("Type your password: ")  # [input] for dumb terminals [getpass] for security
                role = input("Role [super-user] / [common-user]: ")
                print("-=          -           =-=")

                if signin(signInUser, passwd, role):
                    system("cls")
                    print("-> Sign up successful\n")
                else:
                    print("-> User already exists")
            # Shows all the users and their roles
            case "show" | "2":
                system("cls")
                for i in USERS:
                    print(f"user: {i} / role:{USERS[i]['role']}")
            # Remove a specific user
            case "remove" | "3":
                system("cls")
                print("-=          -           =-=      -> Admin remove menu")
                ToRemoveUser = input("Type the username: ")
                print("-=          -           =-=")
                if ToRemoveUser in USERS:
                    if input("Are you sure? y/N\n: ").lower() == "y":
                        del USERS[ToRemoveUser]
                        savefile()
                        system("cls")
                        print("-> User removed")
                    else:
                        print("-> User not removed")
                        system("cls")
                else:
                    print("-> User not found")

            case "exit" | "0":
                system("cls")
                menu(user)
                break

            case _:
                system("cls")
                print("You found it :)")


def menu(user):
    while True:
        print("=-=          -           =-=     -> Menu")
        print("1 - [Go] to another menu (it doesn't exist)")
        print("2 - [About] the program")
        print("3 - About the [admin] user")
        if USERS[user]["role"] == "super-user\n":
            print("4 - Admin [exclusive] menu")
        print("0 - [Exit] or [Logoff]")
        print("=-=          -           =-=")
        option = input(": ").lower()
        print("\n")
        match option:
            case "go" | "1":
                system("cls")
                print("-> There is no menu\n")
            case "about" | "2":
                system("cls")
                print("-> A simple program, with simple login logic and file manipulation\n")
            case "admin" | "3":
                system("cls")
                print("-> It exist, admin user and pass\n")
            case "exclusive" | "4":
                if USERS[user]["role"] == "super-user\n":
                    system("cls")
                    adminmenu(user)
                    break
                else:
                    system("cls")
                    randommessages()
            case "exit" | "0":
                match input("Are you sure? Y/n\n: ").lower():
                    case "n":
                        pass
                    case _:
                        break
            case "logoff":
                system("cls")
                loginmenu()
                break
            case _:
                system("cls")
                randommessages()


def loginmenu():
    readfile()
    print("=-=          -           =-=     -> Login menu")
    print("1 - [Log] in ")
    print("2 - [Sign] up")
    print("0 - [Exit]")
    print("=-=          -           =-=")
    option = input(": ").lower()
    match option:
        case "log" | "1":
            system("cls")

            print("=-=          -           =-=     -> Log in")
            user = input("Type your username: ")
            passwd = input("Type your password: ")  # [input] for dumb terminals [getpass] for security
            print("-=          -           =-=")

            if login(user, passwd):
                system("cls")
                print("-> Login successful\n")
                menu(user)
            else:
                loginmenu()

        case "sign" | "2":
            system("cls")

            print("-=          -           =-=      -> Sing up")
            user = input("Type your username: ")
            passwd = input("Type your password: ")  # [input] for dumb terminals [getpass] for security
            print("-=          -           =-=")

            if signin(user, passwd):
                system("cls")
                print("-> Sign up successful\n")
                loginmenu()
            else:
                print("-> User already exist\n")
                loginmenu()

        case "exit" | "0":
            match input("Are you sure? Y/n\n: ").lower():
                case "n":
                    system("cls")
                    loginmenu()
        case _:
            system("cls")
            loginmenu()


if __name__ == '__main__':
    system("color e")  # changes terminal color to yellow
    system("cls")
    loginmenu()
