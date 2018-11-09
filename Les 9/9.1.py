som=0
count=-1
while True:
    getal=eval(input("noem een getal: "))
    som+= getal
    count+=1
    if getal == 0:
        break

print("Er zijn "+str(count)+" getallen ingevoerd, de som is: "+ str(som))