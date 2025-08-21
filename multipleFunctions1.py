class multipleFunctions:    
    def Subfields():
        a= ['Machine Learning', 'Newral Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for ai in a:       
            print(ai)       
    def OddEven():
        num1=int(input("Enter a Number:"))    
        num2=num1%2    
        if (num2==0):
            print(num1, "is Even number")
        else:
            print(num1,"is number Odd numbet")

    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Enter Your Age:"))
        if (gender=='male' and age>=21 or gender=='female' and age>=18):
            print("Eligible")
        else:
            print("Not Eligible")

    def Percentage():
        sub1=int(input("Enter Tamil Mark:"))
        sub2=int(input("Enter English Mark:"))
        sub3=int(input("Enter Maths Mark:"))
        sub4=int(input("Enter Science Mark"))
        sub5=int(input("Enter Biology Mark"))
        tot=sub1+sub2+sub3+sub4+sub5
        percentage=tot/5
        print("Total=",tot)
        print("Percentage=",percentage)
        
            
     