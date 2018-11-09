try:
    Aantal=eval(input('Met hoeveel mensen ben je op reis geweest?: '))
    bedrag= 4356/Aantal
    print(bedrag)
    if Aantal <0:
        print("Negatieve getallen zijn niet toegestaan!")
except ValueError:
    print("Gebruik cijfers voor het invoeren van het getal!")
except ZeroDivisionError:
    print("Delen door nul kan niet!")
except NameError:
    print("Geef alstublieft een geldig getal op")
except:
    print("Onjuiste invoer")