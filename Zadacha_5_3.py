# Подгрузка модулей

from random import randint
import os

# Функция инициации игры

def game_initiation():
    playerOne = input("Игрок 1. Введите ваше имя: ")
    playerTwo = input("Игрок 2. Введите ваше имя: ")
    hand = randint(0, 2)
    if hand == 0:
        print(f"Первый ходит игрок {playerOne}")
    else:
        print(f"Первый ходит игрок {playerTwo}")
    return [playerOne, playerTwo, hand]

# Функция печати игрового поля 

def game_pad(val): 
    os.system('CLS') 
    print("Давай сыграем в крестики-нолики!")
    print() 
    print('\t     |     |') 
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2])) 
    print('\t_____|_____|_____') 
    
    print('\t     |     |') 
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5])) 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
  
    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8])) 
    print("\t     |     |") 
    print()

#Фунцкия хода

def make_the_move(which_hand, pos):
    make = 0
    if which_hand == 0:
        make = int(input(f"Игрок {player1}, выберите позицию для хода: "))
        pos[make-1] = 'X'
    else:
        make = int(input(f"Игрок {player2}, выберите позицию для хода: "))
        pos[make-1] = 'O'
    return pos

#Проверка на выигрыш
def check_Victory(playerpos):
    victory_positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in range(len(victory_positions)):
        j0 = victory_positions[i][0]
        j1 = victory_positions[i][1]
        j2 = victory_positions[i][2]
        if playerpos[j0-1] == 'X' and playerpos[j1-1] == 'X' and playerpos[j2-1] == 'X':
            print("Выиграл игрок Х")
            return True
        elif playerpos[j0-1] == 'O' and playerpos[j1-1] == 'O' and playerpos[j2-1] == 'O':
             print("Выиграл игрок 0")
             return True
    return False




# Основной текст

# Приглашение к игре

print("Давай сыграем в крестики-нолики!")
position = [1,2,3,4,5,6,7,8,9]
game_pad(position)

# ввод имён и розыгрыш первого хода
init_data = game_initiation()
player1 = init_data[0]
player2 = init_data[1]
hand = init_data[2]

# Операции хода
endGame = False
count = 0
while endGame != True and count < 9:
    count +=1
    if hand == 0:
        position = make_the_move(hand, position)
        game_pad(position)
        endGame = check_Victory(position)
        hand = 1
    else:
        position = make_the_move(hand, position)
        game_pad(position)
        endGame = check_Victory(position)
        hand = 0
    if count >= 9:
        print("Игра окончилась ничьёй")
