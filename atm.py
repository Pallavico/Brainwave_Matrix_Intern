print("welcome to the sbi atm\n please insert your card")
password=int(input("enter your password:"))
if password==1234:
    print("1 for balance enquiry\n 2 for cash withdrawal\n 3 for cash deposit\n 4 for exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("your balance is 10000")
    elif choice==2:
        amount=int(input("enter the amount to withdraw:"))
        print(f"you have withdrawn {amount}")
    elif choice==3:
        amount=int(input("enter the amount to deposit:"))
        print(f"you have deposited {amount}")
    elif choice==4:
        print("thank you for using the atm")
else:
    print("incorrect password, please try again")
