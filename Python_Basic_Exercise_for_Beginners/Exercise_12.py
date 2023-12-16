# Calculate income tax for the given income by adhering to the rules below

# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.


income = int(input("enter income = "))


def count_tex(income):
    payable_tex = 0
    if income<=10000:
        payable_tex = 0
    elif(income<=20000):
        payable_tex = (income-10000) * 10/100
    else:
        payable_tex = 0
        
        payable_tex = 10000 * 10 /100

        payable_tex+=(income - 20000) * 20 /100
    
    print(payable_tex)
    

count_tex(income)