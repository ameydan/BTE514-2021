kilo = int(input("Kilonuzu giriniz:"))
boy = float(input("Boyunuzu giriniz:"))
bmi = kilo / boy ** 2


# a = "T" if 5>3 else "H"

if 18<bmi<24:
    print("Kilonuz iyi")
elif bmi<18:
    print("Kilonuz iyi degil")
    print("Biraz kilo alabilirsiniz")
elif bmi>24:
    print("Kilonuz iyi degil")
    print("Biraz kilo verebilirsiniz")

'''
else:
    print("Kilonuz iyi degil")
    if bmi<=18:
        print("Biraz kilo alabilirsiniz")
    elif bmi>=24:
        print("Biraz kilo verebilirsiniz")
'''
print("Bye!!")