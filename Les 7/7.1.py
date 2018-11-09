def convert(tempC):
    tempF = tempC * 1.8 + 32
    return(tempF)

def table(temp):
    print("  F      C")
    for t in temp:
        convert(t)
        print("{:5} {:5}".format(convert (t), t))

temp = range(-30,41,10)
table(temp)
