def EGP_TO_US(x,y):
    return x*y
def EGP_TO_EURO(x,y):
    return x*y 
def US_TO_EPG(x,y):
    return x*y 
def US_TO_EURO(x,y):
    return x*y 
def EURO_TO_US(x,y):
    return x*y 
def EURO_TO_EGP(x,y):
    return x*y 


dollor=[0.052,1.00]
EURO=[0.052,1.00]
EGP=[19.12,19.12]
print(" Choose the number : ")
print(" 1.EGP TO US ")
print(" 2.EGP TO EURO ")
print(" 3.US TO EURO")
print(" 4.US TO EGP")
print(" 5.EURO TO US ")
print(" 6.EURO TO EGP")
while True:
    choose = input(" ( 1 / 2 / 3 / 4 / 5 / 6 ) : ")

    if choose in ('1','2','3','4','5','6'):
        num1 = float(input(" ENTER THE CASH TO CONVERT : "))
        if choose=='1':
            print(EGP_TO_US(num1,dollor[0] ))

        if choose=='2':
            print(EGP_TO_EURO(num1,EURO[0] ))

        if choose=='3':
            print(US_TO_EURO(num1,EURO[1] ))

        if choose=='4':
            print(US_TO_EPG(num1, EGP[0]))

        if choose=='5':
            print(EURO_TO_US(num1,dollor[1]))             

        if choose=='6':
            print(EURO_TO_EGP(num1, EGP[1]))
    break
