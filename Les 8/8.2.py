list=(input("Geef lijst met minimaal 10 strings: "))
outfile = open("strings.txt", "w")
outfile.write(list)
outfile.close()
infile=open("strings.txt",'r')
regel=infile.readlines()
letters=''
for words in regel:
    woorden=words.split("\", \"")
    outfile = open("strings.txt", 'a')
    outfile.write('\nDe nieuwgemaakte lijst is: ')
    for woord in woorden:
        if len(woord) == 4:
            outfile.write('\''+woord+'\', ')
outfile.close()