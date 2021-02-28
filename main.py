from random import randint
from math import floor
import os

def son_topish():
    i = 1
    j = 1
    son = randint(1, 10)
    num = int(input(f"1 dan 10 gacha son o'yladim topa olasizmi?:\n>>"))
    while son != num:
        i += 1
        if num < son:
            num = int(input("Xato, men o'ylagan son bundan kattaroq, yana harakat qiling:\n>>"))
        else:
            num = int(input("Xato, men o'ylagan son bundan kichikroq, yana harakat qiling:\n>>"))

    print(f"TOPDINGIZ! {son} sonini o'ylagan edim. {i} ta tahmin bilan topdingiz. Tabriklayman! \n")

    print("1 dan 10 gacha son o'ylang men topishga harakat qilaman.\n")
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing.")
    son = randint(1, 10)
    inp = input(f"Siz {son} sonini o'yladingiz: to'g'ri(t), bundan kattaroq(+), kichikroq(-)")
    mx = 11
    mn = 1
    ke = mx
    ek = mn
    while inp != "t":
        if inp == "+":
            ek = son
            son = (son + mx)//2
            mx = ke
        else:
            ke = son
            son = (son + mn)//2
            mn = ek
        inp = input(f"Siz {son} sonini o'yladingiz: to'g'ri(t), bundan kattaroq(+), kichikroq(-)")
        j += 1
    print(f"Soningizni {j} ta tahmin bilan topdim!")

    if i < j:
        print(f"Siz {i} ta tahmin bilan topdingiz va yutdingiz!")
    elif j < i:
        print(f"Men {j} ta tahmin bilan topdim va yutdim!")
    else:
        print(f"Durrang! Ikkimiz ham {i} ta tahmin bilan topdik")

print("Keling o'ylagan sonni topish o'ynaymiz!")
son_topish()
while input("Yana o'ynaymizmi?(yes/no)") != "no":
    son_topish()
