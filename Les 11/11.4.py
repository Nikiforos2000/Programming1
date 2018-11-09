import csv

with open('CSVheader.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    duurste=0
    duursteproduct=[]
    aantal=600
    minste=[]
    voorraad=0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            voorraad += int(row[3])
            if float(row[4]) > float(duurste):
                duurste = row[4]
                duursteproduct = row
            if float(row[3])<float(aantal):
                aantal=row[3]
                minste=row
print('Het duurste artikel is {} en die kost {} Euro'.format(duursteproduct[2],duursteproduct[4]))
print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(minste[3],minste[0]))
print('In totaal hebben wij {} producten in ons magazijn liggen'.format(voorraad))