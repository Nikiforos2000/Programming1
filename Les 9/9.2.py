print("Noem een woord met 4 letters.")
while True:
    woord=input("Noem een woord: ")
    print(woord+" heeft "+str(len(woord))+" letters.")
    if len(woord)== 4:
        break