def seizoen(maandnummer):
    if maandnummer ==12 :
        seizoen = "winter"
    elif maandnummer >=9 :
        seizoen = 'herfst'
    elif maandnummer >=6:
        seizoen = 'zomer'
    elif maandnummer >=3:
        seizoen = 'lente'
    else:
        seizoen = 'winter'
    return seizoen

maandnummer = eval(input("Noem een maandnummer: "))
seizoen(maandnummer)
print('Het is {}.'. format(seizoen(maandnummer)))