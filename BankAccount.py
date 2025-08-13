BALANCE=1000
attempt=4
pincod=9265

while attempt>0:
      
        pin=int(input("ENTERR THE 4 DIGIT PIN: "))  
        if pin==pincod:
                while BALANCE>0:
                    print(f"CURRENT BALANCE: {BALANCE}")
                    WITHDRAWAL = eval(input("ENTER THE WITHDRAWAL AMOUNT: "))
                    if WITHDRAWAL<=0:
                        print("ENTER A POSITIVE INTGER!")
                    elif WITHDRAWAL>BALANCE:
                        print("INSUFFICIENT BALANNCE!")
                    else:
                        BALANCE-=WITHDRAWAL
                        print("WIDTHDRAWAL SUCCESSFUL.")
                        check=input("do you want to contnue yes/no: ").lower
                        if check=="yes":
                            continue
                        else: 
                            break
                else:
                    print("BALANCE IS NOW 0.")
                    break
        else:
            attempt-=1
            print("WRONG PIN\nTRANSTION CANCLED")

else:
     print("YOUR CARD IS TEMPORELY BLOCKED")
