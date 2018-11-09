def standaardprijs(afstandKM):
    if afstandKM > 50:
        bedrag=15+afstandKM*0.60
    else:
        if afstandKM<0:
            afstandKM==0
        bedrag = afstandKM*0.80
    return bedrag

def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == 'zaterdag' or weekendrit =='zondag':
        weekendrit = True
        if leeftijd < 12 or leeftijd > 64:
            #print(standaardprijs(afstandKM) - (standaardprijs(afstandKM) / 100 * 35))
            weekendleeftijd= standaardprijs(afstandKM) - (standaardprijs(afstandKM) / 100 * 35)
            return weekendleeftijd
        else:
            #print(standaardprijs(afstandKM)-(standaardprijs(afstandKM) / 100 * 40))
            weekend=standaardprijs(afstandKM)-(standaardprijs(afstandKM) / 100 * 40)
            return weekend
    else:
        weekendrit = False
        if leeftijd <12 or leeftijd >64:
            #print(standaardprijs(afstandKM)-(standaardprijs(afstandKM)/100*30))
            leeftijdkorting=standaardprijs(afstandKM)-(standaardprijs(afstandKM)/100*30)
            return leeftijdkorting
        else:
            #print(standaardprijs(afstandKM))
            standaard=standaardprijs(afstandKM)
            return standaard

    return


afstandKM=eval(input("Hoeveel kilometer is de reis: "))
#print(standaardprijs(afstandKM))
leeftijd=eval(input("Wat is je leeftijd: "))
weekendrit=input("op welke dag ga je (schrijf zonder hoofdletter): ")
ritprijs(leeftijd, weekendrit, afstandKM)
print(ritprijs(leeftijd, weekendrit, afstandKM))