#WAP to check eligiblity for licence
age=int(input("Enter Age : "))

#if statement

'''
    syntax :

        if condition:
            code...
        else:
            code...   

'''

if age>=18 and age<=50:
    print("Eligible")
elif age>=16 and age<18:
    print("Learning Licence")
elif age>50:
    print("You have Crossed 50 + age limit ")
else:
    print("Not Eligible !!!")
