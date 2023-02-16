# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def takeBonbon(name):
    isCorrect = False
    while not isCorrect:
        try:
            while not isCorrect:
                numBons = int(input(f"{name}, введите от 1 до 28 конфет: "))
                if numBons < 1 or numBons > 28:
                    print("Число должно быть от 1 до 28")
                else:
                    isCorrect = True
        except ValueError:
            print("Это не число!")
    return numBons

def smartBotTakesBons(value):
    numBons = value % 28 - 1
    if numBons == 0:
        numBons = 28
    return numBons

def stepResult(player, bons, playerHand, onTable):
    print(f"{player} взял {bons} конфет. У него теперь {playerHand}. На столе осталось {onTable}.")

playerOne = input("Игрок, введите ваше имя: ")
playerTwo = str('Smart Botik')
print(f"Привет, {playerOne}, меня зовут {playerTwo}!")
playerOneBons = 0
playerTwoBons = 0
bonsOnTable = 341
hand = randint(0, 2)

if hand:
    print(f"Ходит {playerOne}")
else:
    print(f"Ходит {playerTwo}")

while bonsOnTable > 28:
    if hand:
        bonsTaken = takeBonbon(playerOne)
        playerOneBons += bonsTaken
        bonsOnTable -= bonsTaken
        hand = False
        stepResult(playerOne, bonsTaken, playerOneBons, bonsOnTable)
    else:
        bonsTaken = smartBotTakesBons(bonsOnTable)
        playerTwoBons += bonsTaken
        bonsOnTable -= bonsTaken
        hand = True
        stepResult(playerTwo, bonsTaken, playerTwoBons, bonsOnTable)

if hand:
    print(f"{playerOne} выиграл")
else:
    print(f"{playerTwo} выиграл")