# Write a function called exponent(base, exp) that returns an int value 
# of base raises to the power of exp.

def exponent(base, exp):
    print(f"{base} raise to the power {exp} : {base**exp}")

    num = exp
    result = 1
    while num>0:
        result = result * base
        num-=1
    print(result)


exponent(5,4)


