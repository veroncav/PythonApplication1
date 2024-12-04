# # from calendar import monthrange
# # from datetime import*
# from random import *
# from math import *

# # tana=date.today().strftime("%B %d, %Y")

# # print(f"Tere! Täna on {tana}")
# # d=tana.day
# # m=tana.month
# # y=tana.year

# # print(d)
# # print(m)
# # print(y)


# # detsP=monthrange(2024,12)[1] #31
# # novP=monthrange(2024,11)[1] #30
# # jaak=detsP+novP-d
# # print(f"Aasta lõppuni on {jaak}")
# # print(f"Aasta kuu on {jaak2}")

# # Ülesanne 2
# # vastus1=3 + 8 / (4-2) * 4 
# # vastus2=3 + 8 / 4-2 * 4 
# # vastus3=(3 + 8) / (4-2) * 4 
# # vastus3=round((3 + 8 / (4-2) * 4)
# # print(vastus1,"\n"vastus2,"\n",vastus3,"\n", vastus4)

# #Ülesanne 3
# #1 variant
# try:
#    R=float(input("Sisesta R: "))
#    Sk=pi*R**2
#    Lk=2*pi*R
#    Skv=(2*R)**2
#    Lkv=(2*R)*4
#    print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")
# except:
#     print("On vaja number!")


# #2 varint
# R=random()*100 #0.0....1.0
# print(f"R={R}")
# Sk=pi*R**2
# Lk=2*pi*R
# Skv=(2*R)**2
# Lkv=(2*R)*4
# print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")

# #Ülesanne 4
# d=2.575 #mundi d sm+
# maa=6378 #maa radius km
# maa*=100000 #maa radius sm+maa=maa*100000
# Lmaa=2*pi*maa
# kogus=int(Lmaa/d)
# print(f"On vaja {kogus}mundi.\nMeil on vaja {kogus*2}eur")


import  math # * from не нужен
print("Ruudu karakteristikud:") #Где нужно вводить ответ добавила (:)
try: #добавила try для проверки типа данных
a=float(input("Sisesta ruudu külje pikkus => ")) #нужно добавить двойные кавычки (") вместо (')
# а так же все вводимые данные преобразую в float
S=a**2
print("Ruudu pindala:", S)
P=4*a
print("Ruudu ümbermõõt:", P)  #Вместо таких (' ') скобок ставим (")
di=a*math.sqrt(2) #sgrt вместо sgt
print("Ruudu diagonaal:", round(di,2))
except ValueError: # Добавила для обработки ошибок, связанных с неправильным вводом данных
 #(например ввод букв, вместо числ) вместо ошибки, программа выдаст сообщение Palun sisestage arvuline väärtus!
print("Palun sisestage arvuline väärtus!")

print("\nRistküliku karakteristikud:")) # Добавила \n для перехода на новую строку

try: #добавила try для проверки типа данных как и выше
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #все вводимые данные преобразую в float
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print(Ristküliku pindala', S)
P=2*(b+c) # Добавила знак умножения чтоюы формула работала корректно*
print("Ristküliku ümbermõõt:", P)
di=math.sqrt(b**2+c**2) # Исправила на ** чтобы возвести в степень.
print("Ristküliku diagonaal:", round(di)
except ValueError: # Сделала тоже самое что и выше
print("Palun sisestage arvuline väärtus!")

print("\nRingi karakteristikud") # Так же добавила \n для перехода на новую строку

try:# тоже добавила try для проверки типа данных
r=float(input("Sisesta ringi raadiusi pikkus => ")) #Поменяла ковычки и добавила float
d=2*r #Добавила * для корректной формулы
print("Ringi läbimõõt:" d)
S=pi()*r*2
print("Ringi pindala:", round(S))
C=2pi()*r
print("Ringjoone pikkus:", round(C)