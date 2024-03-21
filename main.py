from random_answer import answer
from calculator import calc

def main():
    while True:
        which_tools = input("""
List tools:
1. Random answer
2. Calculator
3. Exit tools

Which tool you want use? """)

        log_exit = "\nSuccess exit."
        match which_tools:
            case "1":
                while True:
                    answer()
                    ulangi = input("Ulangi (Y/n)? \n")
                    if ulangi == "n":
                        break
            case "2":
                calc()

            case "3":
                print(log_exit)
                break  # Exit the main loop here
            case '':
                print(log_exit)
                break  # Exit the main loop here

if __name__ == "__main__":
    main()
