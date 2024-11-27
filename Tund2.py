# from calendar import monthrange
# from datetime import*



# tana=date.today().strftime("%B %d, %Y")

# print(f"Tere! Täna on {tana}")
# d=tana.day
# m=tana.month
# y=tana.year

# print(d)
# print(m)
# print(y)


# detsP=monthrange(2024,12)[1] #31
# novP=monthrange(2024,11)[1] #30
# jaak=detsP+novP-d
# print(f"Aasta lõppuni on {jaak}")
# print(f"Aasta kuu on {jaak2}")

# Ülesanne 2
# vastus1=3 + 8 / (4-2) * 4 
# vastus2=3 + 8 / 4-2 * 4 
# vastus3=(3 + 8) / (4-2) * 4 
# vastus3=round((3 + 8 / (4-2) * 4)
# print(vastus1,"\n"vastus2,"\n",vastus3,"\n", vastus4)

#Ülesanne 3
#1 variant
try:
   R=float(input("Sisesta R: "))
   Sk=pi*R**2
   Lk=2*pi*R
   Skv=(2*R)**2
   Lkv=(2*R)*4
   print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")
except:
    print("On vaja number!")


    #2 varint
     R=random()*100 #0.0....1.0
     print(f"R={R}")
   Sk=pi*R**2
   Lk=2*pi*R
   Skv=(2*R)**2
   Lkv=(2*R)*4
   print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}")
except:
    print("On vaja number!")
#3333