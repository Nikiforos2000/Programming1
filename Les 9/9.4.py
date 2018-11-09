infile=open('ticker.txt','r')
inhoud=infile.readlines()
infile.close()

dictionary={}

def ticker(filename):
    for gedeelte in inhoud:
        inhoud_split=gedeelte.split(":")
        dictionary[inhoud_split[0]]=inhoud_split[1].strip()
    return dictionary
print(ticker(dictionary))
company=input("Enter Company name: ")
print('Ticker symbol: '+dictionary[company])
Ticker=input("Enter Ticker symbol: ")
for bedrijf in dictionary.keys():
    if Ticker == dictionary[bedrijf]:
        print('Company name: '+bedrijf)