from keylogger import keylog

def main():
    while True:
        print("Welcome")
        print("1. Keylogger")
        print("2. Exit")
        choice = input("\nENTER YOUR CHOICE~# ")

        match choice:
            case '1':
                keylog()
            case '2':
                break
            case _:
                print("Invalid choice!")
                
if __name__== "__main__":
    main()