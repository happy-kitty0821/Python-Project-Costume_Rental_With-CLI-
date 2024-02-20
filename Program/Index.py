import time #importing python inbuilt module
import Rent #importing functionality from other project file
import Return#importing functionality from other project file

def index():#this is the main function of the program everything starts from here
    while True:
        try:
            choice = int(input("""
__________________________                 
|   Task you want to do? |
__________________________
|   1 for: Display       |
|   2 for: Rent          |
|   3 for: Return        |
|   4 for: Exit          |
__________________________  
 >>> """))
            if choice == 1:
                with open("CostumeDetail.txt", "r") as f:
                    print(f.read())
            elif choice == 2:
                a = Rent.costume_key()
                b = Rent.user_input_for_rent()
                continue_rent = True
                while continue_rent:
                    Rent.display_costume(b)
                    Rent.rent(a, b)
                    Rent.var(a)
                    Rent.set_invoice(a)
                    continue_rent = input("Do you want to rent costume again? [Yes]-'y' [no]-'n': ").lower() == 'y'
                Rent.handle_last_part_of_invoice()
                print("Thank you for renting from us. Visit again :)")
            elif choice == 3:
                dic = Return.costume_key()
                Return.user_input_for_return()
                Return.user_input()
                continue_return = True
                while continue_return:
                    dic_up = Return.add_quantity(dic)
                    Return.var(dic_up)
                    Return.set_invoice(dic)
                    continue_return = input("Do you want to return costume again? [Yes]-'y' [no]-'n': ").lower() == 'y'
                Return.handle_last_part_of_invoice()
                print("Thank you for returning. Visit again :)")
            elif choice == 4:
                break
            else:
                print("Choose a valid option from the above four options")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("Do you want to exit the program? [Y]/[N]")
            ctrl_choice = input(">>> ").capitalize()
            if ctrl_choice == "Y":
                time.sleep(2)
                print("Exiting.....")
                break
            else:
                print(f"Invalid input {ctrl_choice}")

if __name__ == "__main__":
    index()
else:
    print("[+] Error during the execution of the program [+]")
