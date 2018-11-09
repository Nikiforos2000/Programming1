list=[1,2,3,4,5,6,7,8,9,10]

for number in list:
    for number1 in list:
        print("{} + {} = {}".format(number, number1, number*number1))