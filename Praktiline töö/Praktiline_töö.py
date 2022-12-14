#1
from math import *
from random import *
num=int(input("Enter a number:"))
if num>=0:
	if num%2==0:
		print("isegi")
else:
	print("kummaline")

#2
num1 = int(input("Esimene number: "))
num2 = int(input("Teine number: "))
num3 = int(input("Kolmas number: "))
if num1 > 0 and num2 > 0 and num3 > 0:
    if num1 + num2 + num3 == 180:
        if num1 == num2 and num2 == num3:
            print("Arvud tähistavad võrdkülgse kolmnurga nurki..")
        elif num1 == num2 or num1 == num3 or num2 == num3:
            print("Arvud tähistavad võrdhaarse kolmnurga nurki..")
        else:
            print("Numbrid tähistavad skaala kolmnurga nurki..")
    else:
        print("Mitte nurgad!")
else:
    print("Viga!")

#3
kusimus = input("mis nädalapäev? ")
if kusimus.lower() == "jah":
  number = input("Sisestage arv vahemikus 1 kuni 7: ")
  if number.isdigit() and 1 <= int(number) <= 7:
    days = ["Esmaspäev, Teisipäev, Kolmapäev, Neljapäev, Reede,Laupäev, Pühapäev"]
    print(f"nädalapäev: {days[int(number)-1]}")
  else:
    print("viga!")
else:
  print("hed aega")

#4
