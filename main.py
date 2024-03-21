from random_answer import answer

def main():
    while True:
        which_tools = input("""
List tools:
1. Random answer
2. Exit tools

Which tool you want use? """)

        log_exit = "\nSuccess exit."
        match which_tools:
            case "1":
                while True:
                    answer()
                    ulangi = input("Ulangi (Y/n)? \n")
                    if ulangi == "n":
                        break
            case "2" or '':
                print(log_exit)
                break  # Exit the main loop here
            case '':
                print(log_exit)
                break  # Exit the main loop here

if __name__ == "__main__":
    main()
