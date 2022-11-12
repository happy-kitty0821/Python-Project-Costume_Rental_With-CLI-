# importing datetime from datetime module 
import datetime
data=datetime.datetime.now()
# function for creating dictionary
def costume_key():
    file=open("CostumeDetail.txt","r")
    dictonary={}
    set=1
    for new in file:
        dictonary[set]= new.replace("\n","").split(",")
        set+=1
    
    return dictonary

# function for displaying in tabular form
def display_costume(flag):
    while flag:
        print("set\t\tName \t\t Brand\t\tPrice\t\tQuantity")
        costumes=costume_key()
        # itterrating the dictionary
        for key, values in costumes.items():
            print(key,end="\t")
            for set in range(len(values)):
                if set in (2,3):
                    print(f"{values[set]}",end="\t\t")
                else:
                    print(f"{values[set]}",end="\t\t")
            print()
            print()
        print("You can rent the costume from above table")
        flag=False

# functions for customer details input
def user_input_for_rent():
    global client_name
    global flag
    flag=True
    while flag:
        client_name=input("""
__________________________________________________
Enter customer Name:                              
 >>> """)
        Customer_name=client_name.replace(" ","")
        if Customer_name=="":
            flag=True
            print("Please input customer Name")
        else:
            # checking name is alphabet or not
            if Customer_name.isalpha():
                # creating new text file and writing on it
                new=client_name+".txt"
                with open(new,"w") as a:
                    # creating invoice format
                    a.write("""
x-------------------------------------ABC COSTUME RENTAL STORE-------------------------------------x
    ---------------------------------Sundarharaincha-03, Morang---------------------------------
    
          """)
                    a.write("Customer Name: "+client_name+"\t\t\t\t\t\t\t\t\t\t\tDate: "+data.strftime('%m/%d/%Y')+"\n\n") 
                    a.write("\t\t\tName of Costume\t\tName of Brand\t\t Price\t\t Quantity\t\t Total\n\n")   
                                   
                break
            else:
                print("Input String value for Customer Name")
                flag=True
    return flag

#function for set number and quantity          
def rent(dictionary,flag):
    while flag:
        try:
            global set_no
            set_no=int(input("""
__________________________________________________
Enter the set no of costume you want to rent.
 >>> """))
            # itterating the dictionary
            for key,value in dictionary.items():
                # check set_no to key
                if key==set_no:
                    try:
                        b=True
                        while b:
                            global quantity
                            quantity=int(input("""
___________________________________________________
Enter the quantity
 >>> """))
                            # passing quantity in q variable
                            q=int(value[3])
                            if quantity<=0:
                                b=True
                                print("Please input positive value in quantity")
                            elif quantity<=q:
                                sq=int(dictionary[key][3])
                                # subtracting quantity with sq values
                                sq-=quantity
                                dictionary[key][3]=sq
                            
                                b=False
                                flag=False
                                break
                            else:
                                print("""
_________________________________________________________
Out of stock of quantity / see costume details carefully|
_________________________________________________________
                                      """)
                                b=True
                    except:
                        print("""
___________________________________________________
Enter integer value in quantity                   |
___________________________________________________
""")          
        except:
            print("""
___________________________________________________
Please input valid set_no                         |
___________________________________________________
                  """)
    return 

# function for updating dictionary
def var(dictionary):
    C="CostumeDetail.txt"
    with open(C,"w") as a:
        for value in dictionary.values():
            for i in range(len(value)):
                if i==3:
                    a.write(str(value[i])+"\n")
                else:
                    a.write(str(value[i])+",")


grand_total = 0

# function for creating invoice
def set_invoice(dictionary):
    global grand_total
    C=client_name+".txt"
    with open(C,"a+") as a:
        # passing the values of a certain key
        values = dictionary[set_no]
        Costume_Name= values[0]
        Brand=values[1]
        Price=values[2]
        Price_=Price.replace("$","")
        Total=str(int(Price_)*quantity)
        grand_total  = grand_total + int(Total)
        Quantiy_=str(quantity)
        # writing on the invoice
        #  if else is for maintain spacing
        if set_no==1:
            a.write("\t\t\t"+Costume_Name+"\t\t"+Brand+"\t\t\t "+Price+"\t\t\t"+Quantiy_+"\t\t\t $"+Total+"\n")
        elif set_no==2:
            a.write("\t\t\t"+Costume_Name+"\t\t"+Brand+"\t\t\t"+Price+"\t\t\t"+Quantiy_+"\t\t\t $"+Total+"\n")
        else:
            a.write("\t\t\t"+Costume_Name+"\t\t"+Brand+"\t\t"+Price+"\t\t\t"+Quantiy_+"\t\t\t $"+Total+"\n")   
    print("""
++++++++++++++++++++++++
Rented Succesfully     +
++++++++++++++++++++++++""")

#functions for grand total   
def handle_last_part_of_invoice():
    global grand_total
    # parsing grand_total to string to write in invoice
    str_to_grand_total=str(grand_total)
    C=client_name+".txt"
    with open(C,"a+") as a:
        a.write("\n")
        a.write("""                                                                              _________""")
        a.write("\n")
        a.write("                                                                Grand Total:     $"+str_to_grand_total+"\n")
    grand_total=0