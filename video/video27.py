import random

while(True):
    lanjut = input("Lempar dadu? y/n: ")

    if(lanjut == "y"):
        print(random.choice([1, 2, 3, 4, 5, 6]))
    elif (lanjut == "n"):
        break
    else:
        print("Ketik y atau n dong kakack")
