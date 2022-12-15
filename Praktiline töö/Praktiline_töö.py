from math import *
from random import *
#1
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
            print("Arvud tдhistavad vхrdkьlgse kolmnurga nurki..")
        elif num1 == num2 or num1 == num3 or num2 == num3:
            print("Arvud tдhistavad vхrdhaarse kolmnurga nurki..")
        else:
            print("Numbrid tдhistavad skaala kolmnurga nurki..")
    else:
        print("Mitte nurgad!")
else:
    print("Viga!")

#3
kusimus = input("mis nдdalapдev? ")
if kusimus.lower() == "jah":
  number = input("Sisestage arv vahemikus 1 kuni 7: ")
  if number.isdigit() and 1 <= int(number) <= 7:
    days = ["Esmaspдev, Teisipдev, Kolmapдev, Neljapдev, Reede,Laupдev, Pьhapдev"]
    print(f"nдdalapдev: {days[int(number)-1]}")
  else:
    print("viga!")
else:
  print("hed aega")

#5
num = input("Цифру: ")
if num.isalpha():
    print("num")
elif num.isdigit():
    if num.is_integer():
        num = int(num)
        num = num // 2
        print("num")
else:
    num = float(num)
    num = num * 0.7
    print("num")
else:
print("Viga!")

#4
päev = int(input("sünnipäev?: "))
kuu = input("sünnikuu?: ")
if kuu == 'detsember':
	märk = 'Kaljukits' if (päev < 22) else 'Kaljukits'
elif kuu == 'jaanuar':
	märk = 'Veevalaja' if (päev < 20) else 'Veevalaja'
elif kuu == 'veebruar':
	märk = 'kala' if (päev < 19) else 'kala'
elif kuu == 'märts':
	märk = 'jäär' if (päev < 21) else 'jäär'
elif kuu == 'aprill':
	märk = 'härg' if (päev < 20) else 'härg'
elif kuu == 'mai':
	märk = 'Gemini' if (päev < 21) else 'Gemini'
elif kuu == 'juuni':
	märk = 'vähk' if (päev < 21) else 'vähk'
elif kuu == 'juuli':
	märk = 'lõvi' if (päev < 23) else 'lõvi'
elif kuu == 'august':
	märk = 'neitsi' if (päev < 23) else 'neitsi'
elif kuu == 'september':
	märk = 'kaal' if (päev < 23) else 'kaal'
elif kuu == 'oktoober':
	märk = 'Scorpio' if (päev < 23) else 'Scorpio'
elif kuu == 'november':
	märk = 'Ambur' if (päev < 22) else 'Ambur'
print("teie märk:",märk) 

#kõik