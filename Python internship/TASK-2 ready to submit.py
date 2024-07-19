while True:
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    choice=input("Enter the choice from[+,-,*,/,%,//,**] : ")
    while choice not in ('+','-','*','/','%','//','**'):
        print("Invalid choice Enter a valid choice")
        choice=input("Enter the choice from[+,-,*,/,%,//,**] : ")
    if(choice=='+'):
        print("Result = ",num1+num2)
    elif(choice=='-'):
        print("Result = ",num1-num2)
    elif(choice=='*'):
        print("Result = ",num1*num2)
    elif(choice=='/'):
        print("Result = ",num1/num2)
    elif(choice=='%'):
        print("Result = ",num1%num2)
    elif(choice=='//'):
        print("Result = ",num1//num2)
    elif(choice=='**'):
        print("Result = ",num1**num2)
    option=input("DO YOU WANT TO CONTINUE OR NOT YES/NO : ").lower()
    if option != 'yes':
        print("THANKYOU")
        break
