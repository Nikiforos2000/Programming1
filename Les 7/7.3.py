infile= open('Kaartnummers.txt','r')
regels = infile.readlines()
infile.close()
count=0
count1=0
hoogste=0
for regel in regels:
    kaartinfo = regel.split(', ')
    count = count + 1
    if int(kaartinfo[0])> int(hoogste):
        hoogste=kaartinfo[0]
        count1=count


print('Deze file telt {} regels. \nHet grootste kaartnummer is: {} en dat staat op regel {}.'.format(count,hoogste,count1))