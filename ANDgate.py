print('| INPUT | OUTPUT |')
while True:    
    a=int(input("enter input: "))
    b=int(input("enter second input:"))
    i=input("want to contnue (y/n): ")
    
    if (a==1 or a==0) and (b==1 or b==0):
        
        if a==1 and b==1:
            print(f"| {a} | {b} | 1      |")
        else:
            print(f"| {a} | {b} | 0      |")
        if i=='n':
            break
        else:
            continue
    else:
        print("ENTRE BINARY INPUTS!")
