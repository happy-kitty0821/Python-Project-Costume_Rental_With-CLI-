# import datetime from datetime module
from datetime import datetime
# functions for creating dictionary
def costume_key():
    file=open("CostumeDetail.txt","r")
    # creating new dictionary
    dictonary={}
    set=1
    for new in file:
        dictonary[set]= new.replace("\n","").split(",")
        set+=1
    return dictonary

# functions for user detail
def user_input_for_return():
    flag=True
    while flag:
        client_name_for_return=input("""
__________________________________________________
Enter customer Name:                              
 >>> """)
        global cust_name
        # for removing space in name
        cust_name=client_name_for_return.replace(" ","")
        if cust_name =="":
            print("Please enter your Name")
            flag=True
        # check alphabet
        elif cust_name.isalpha():
            # create new file
            new="Return_"+cust_name+".txt"
            with open(new,"w") as a:
                # create format of the invoice
                a.write("""
x-------------------------------------ABC COSTUME RENTAL STORE-------------------------------------x
    ---------------------------------Sundarharaincha-03, Morang---------------------------------
    
          """)
                a.write("Customer Name: "+client_name_for_return)
                a.write("\n")
                a.write("\t\t\tName of Costume\t\tName of Brand\t\t Price\t\t Quantity\t\t Total\n\n")
                break 
        else:
            print("Please input Customer Name as String.")
            flag=True
                
# functions for user input and validation of 
def user_input():
    flag=True
    while flag:
        try:
            rented_date_=input("""
__________________________________________________
Enter the rented date of costume [YYYY/MM/DD]
 >>> """)
            # keeping data in each variable seperated with '-'
            yyyy,mm,dd=rented_date_.split("/")
            mm=int(mm)
            dd=int(dd)
            yyyy=int(yyyy)
            date=datetime.today().date()
            present_date=str(date).replace("-","/")
            # convert string to date object
            d1 = datetime.strptime(present_date, "%Y/%m/%d")
            d2 = datetime.strptime(rented_date_, "%Y/%m/%d")
            # validation for rented date
            if mm>12 and dd>32 and yyyy> 2023:
                print("Input valid date")
            elif d2>d1:
                print("Don't try to go in future.")
            elif mm >13:
                print("Input valid month")
            elif dd >32:
                print("Input valid day")
            elif yyyy > 2023 or yyyy<1990:
                print("Input valid year")
            else:
                flag=False    
                diff= d1-d2
                global day
                day=diff.days
                      
        except:
            print("Please input valid date.")
            flag=True

 
#   function for quantity of returning
def add_quantity(dictonary):  
    try:
        global set_no
        set_no=int(input("""
__________________________________________________
Enter the set no of costume you want to return.
 >>> """))
        # itterateing the dictionary
        for key,values in dictonary.items():
            if key==set_no:
                try:
                    loop=True
                    while loop:
                        global quantity_return
                        quantity_return=int(input("""
___________________________________________________
Enter the quantity to return
 >>> """))
                        if quantity_return<=0:
                            print("Please input positive value in quantity")
                            loop=True
                        else:
                            loop=False
                            # set quantity of costume in variable
                            sq=int(dictonary[key][3])
                            # adding with new returned costume
                            sq+=quantity_return
                            # updating quantity value
                            dictonary[key][3]=sq
                except:
                        print("Enter valid value in quantity")
    except:
        print("Please input valid info")
    return dictonary

grand_total=0
# for appending details in invoice
def set_invoice(dictonary):
    global day
    C="Return_"+cust_name+".txt"
    with open(C,"a+") as a:
        global grand_total
        # passing value of a certain key
        values = dictonary[set_no]
        Costume_Name= values[0]
        Brand=values[1]
        Price=values[2]
        #remove '$' sign for calculation
        Price_=Price.replace("$","")
        Total=str(int(Price_)*quantity_return)
        grand_total  = grand_total + int(Total)
        Quantiy_=str(quantity_return)
        # append details in the format of the invoice
        if set_no==1:
            a.write("\t\t\t"+Costume_Name+"\t\t"+Brand+"\t\t\t "+Price+"\t\t\t"+Quantiy_+"\t\t\t $"+Total+"\n")
        elif set_no==2:
            a.write("\t\t\t"+Costume_Name+"\t\t"+Brand+"\t\t\t"+Price+"\t\t\t"+Quantiy_+"\t\t\t $"+Total+"\n")
        else:
            a.write("\t\t\t"+Costume_Name+"\t\t"+Brand+"\t\t"+Price+"\t\t\t"+Quantiy_+"\t\t\t $"+Total+"\n")   

# functions  for updating the dictionary with updated values
def var(dictonary):
    C="CostumeDetail.txt"
    with open(C,"w") as a:
        for value in dictonary.values():
            for i in range(len(value)):
                if i==3:
                    a.write(str(value[i])+"\n")
                else:
                    a.write(str(value[i])+",")


#functions for calculating total amount 
def handle_last_part_of_invoice():
    global grand_total
    if day<5:
        # total amount without extra charge
        str_to_grand_total=str(grand_total)
        C="Return_"+cust_name+".txt"
        with open(C,"a+") as a:
            a.write("\n")
            a.write("""                                                                              _________""")
            a.write("\n")
            a.write("                                                                Grand Total:     $"+str_to_grand_total+"\n")
        grand_total=0
    else:
        # total amount with extra charge
        # set fine as $2 per day
        fine=2
        fine_day=day-5
        total_fine=fine_day*fine
        str_total_fine=str(total_fine)
        grand=grand_total+total_fine
        str_to_grand=str(grand)
        C="Return_"+cust_name+".txt"
        with open(C,"a+") as a:
            # append calculated data in format of the invoice
            a.write("\n")
            a.write("""                                                                              _________""")
            a.write("\n")
            a.write("                                                                Late Days:        "+str(fine_day)+"\n")
            a.write("                                                                Extra Charge:    $"+str_total_fine+"\n")
            a.write("""                                                                              _________""")
            a.write("\n")
            a.write("                                                                Grand Total:     $"+str_to_grand+"\n")
        grand_total=0
        
