while True:
    a=eval(input("enter the first number: "))
    o=input("enter the operation : ")
    b=eval(input("enter the second number: "))
    if o== "+":
        print(a,o,b,"=",a+b)
    elif o== "-":
        print(a,o,b,"=",a-b)
    elif o== "*":
        print(a,o,b,"=",a*b)
    elif o== "/":
        print(a,o,b,"=",a/b)
        
    else:
        print("choose correct operatar")
    i=input("DO YOU WANT TO CONTNUE(Y/N): ")
    if i=='y' or i=='Y':
        continue
    else:
        break
