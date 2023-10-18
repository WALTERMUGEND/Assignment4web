# maths, physics, geo, Chem
num1 = int(input("Enter the score in maths :\n"))
num2 = int(input("Enter the score in physics :\n"))
num3 = int(input("Enter the score in geo :\n"))
num4 = int(input("Enter the score in chem :\n"))

score = num1 + num2 + num3 + num4

num = score/4
if num<=100 and num>=80:
    print(' You are a Genious and You got A+ grade!')
    breakpoint()

elif num<79 and num>75:
    print('You got A grade')
    breakpoint()

elif num < 75 and num > 70:
    print('You got A- grade')
    breakpoint()
elif num < 70 and num > 65:
    print('You got B+ grade')
    breakpoint()
elif num < 65 and num > 60:
    print('You got B grade')
    breakpoint()
elif num <60 and num >50:
    print('You got C+ grade')
    breakpoint()
elif num <50 and num >40:
    print('You got C grade')
    breakpoint()
elif num<0:
    print('Invalid Option!')
    breakpoint()

else :
    print('Sorry! You are fail')