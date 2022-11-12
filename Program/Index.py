# This is the main file of the project. 
# importing the others sub files
import Rent
import Return
# function for choosing the options
def index():
    check=True
    while check:
        try:
            choice=int(input("""
__________________________                 
|   Task you want to do? |
__________________________
|   1 for: Display       |
|   2 for: Rent          |
|   3 for: Return        |
|   4 for: Exit          |
__________________________  
 >>> """))
            if choice ==1:
                # read the text file
                f=open("CostumeDetail.txt","r")
                print(f.read())
            elif choice ==2:
                # call methods of Rent.py file
                a=Rent.costume_key()
                b=Rent.user_input_for_rent()
                continue_rent=True
                while continue_rent:
                    Rent.display_costume(b)
                    Rent.rent(a,b)
                    Rent.var(a)
                    Rent.set_invoice(a)
                    bl=True
                    while bl:
                        again=input("""
______________________________________________________
Do you want to rent costume again? [Yes]-'y' [no]-'n'|
______________________________________________________
 >>> """)
                        if again.isalpha():
                            if again.lower()=='y':
                                continue_rent=True
                                bl=False
                                # check=False
                            elif again.lower()=='n':
                                continue_rent=False
                                bl=False
                                # calling method for calculating total
                                Rent.handle_last_part_of_invoice()
                                print("""
++++++++++++++++++++++++++++++++++++++++++++++++
+ THANK YOU FOR RENTING FROM US. VISIT AGAIN :)+
++++++++++++++++++++++++++++++++++++++++++++++++""")
                            else:
                                continue_rent=False
                                print("Input valid option")
                                bl=True
                        else:
                          bl=True
                          print("Please choose valid option.")
                            
                                
            elif choice ==3:
                # call methods of Return.py file
                # returns dictionay from costume_key as dic
                dic=Return.costume_key()
                Return.user_input_for_return()
                Return.user_input()
                continue_return=True
                while continue_return:
                    dic_up=Return.add_quantity(dic)
                    Return.var(dic_up)
                    Return.set_invoice(dic) 
                    ag=True
                    while ag:
                        return_again=input("""
______________________________________________________
Do you want to return costume again? [Yes]-'y' [no]-'n'|
______________________________________________________
 >>> """)
                        if return_again.isalpha():
                            if return_again.lower()=='y':
                                continue_return=True
                                ag=False
                            elif return_again.lower()=='n':
                                continue_return=False
                                ag=False
                                # calling method for calculating total with or without extra charge
                                Return.handle_last_part_of_invoice()
                                print("""
+++++++++++++++++++++++++++++++++++++++++++
+ THANK YOU FOR RETURNING. VISIT AGAIN :)+
+++++++++++++++++++++++++++++++++++++++++++""")
                            else:
                                continue_return=False
                                print("Input valid option")
                                ag=True
                        else:
                          ag=True
                          print("Please choose valid option.")
                               
            elif choice ==4:
                # terminate program 
                break
            else:
                print("Choose valid option from above four options")
        except:
            print("Please see the options carefully.") 
        b=True    
        while b:
            option=input("""
__________________________________________________
Do you want to continue again? [Yes]-'y',[No]-'n'|
__________________________________________________
 >>> """)
            if option.isalpha():
                if option.lower()=='y':
                    check=True
                    b=False
                elif option.lower()=='n':
                    # terminate program
                    check=False
                    b=False
                else:
                    print("Please enter value from the two options")
                    b=True
            else:
                print("Please see the options carefully")
                b=True
index()