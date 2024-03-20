from random_answer import answer

which_tools = input("""
List tools:
1. Random answer
2. Exit tools (default)

Which tool you want use? """)

log_exit = "\nSuccess exit."
match which_tools:
    case "1" :
        while True:
            answer()
            ulangi = input("Ulangi (Y/n)? \n")
            if ulangi == "n":
                print(log_exit)
                break
    case "2":
        print(log_exit)
        exit()
    case '':
        print(log_exit)
        exit()
