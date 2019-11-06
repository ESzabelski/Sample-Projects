


number=input("print a number to convert")

def numberconverter(num):
    roman=""



#50 to 99
    if num>=90 and num<100:
        num=num-90
        roman=roman+"XC"
    while num>=50 and num<90:
        num=num-50
        roman = roman+"L"


    #sub50 section
    if num>=40 and num<50:
        num=num-40
        roman=roman+"XL"
    while num>=10 and num<40:
        num=num-10
        roman = roman+"X"

    #single digit handler
    if num>5 and num<10:
        if num==9:
            num=num-9
            roman = roman+"IX" 
        elif num==8:
            num=num-8
            roman = roman+"VIII"
        elif num==7:
            num=num-7
            roman = roman+"VII"
        elif num==6:
            num=num-6
            roman = roman+"VI"             
    if num==5:
        roman = roman+"V"
    elif num==4:
        roman=roman+"IV"
    elif num==3:
        roman=roman+"III"
    elif num==2:
        roman=roman+"II"
    elif num==1:
        roman=roman+"I"

        
    
    return roman



print(numberconverter(int(number)))
