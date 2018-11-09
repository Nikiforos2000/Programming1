naam = input("Wat is je naam: ")
outfile = open("hardloper.txt", "a")
import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, "+naam +"\n")

outfile.write(s)
outfile.close()