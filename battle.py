__author__ = 'edokuchaev'

# set number and size of ships
count = 2
size = 2
board_size = 10

# game over function
def game_over(board):
    user_ships = 0
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 1:
                user_ships += 1
    return user_ships == 0

# print the board function
def print_board(board):
    for i in range(len(board)-1,-1,-1):
        print(board[i])

# set ships on the field
def set_ships(count, size, board, player):
    c = 0
    s = 0
    while c < count:
        print('Set the ships for player', player)
        print('Ship #',c+1,'of total', count, 'ships')
        s = 0
        while s < size:
            print('Input coordinates of cell',s+1,'of total cells',size)
            try:
                coordinates = list(map(int,input().split()))
                if board[coordinates[0]][coordinates[1]] != 1:
                    board[coordinates[0]][coordinates[1]] = 1
                    s+=1
                else:
                    print('This cell is occupied by existing ship, try again')
            except:
                print('Input typo or out of field, try again')
        print('Ship',c+1,'is set')
        c+=1
    print('Ships for player', player, 'are set. The field looks as follows:')
    print_board(board)

# shooting function
def shoot(board, player):
    go_on_shooting = True
    while go_on_shooting:
        try:
            print('Player',player,'shoot!')
            shoot = list(map(int,input().split()))
            if board[shoot[0]][shoot[1]] == 1:
                print('The shoot hit the ship!')
                board[shoot[0]][shoot[1]] = 0
                if not game_over(board):
                    print_board(board)
                else:
                    print('VICTORY OF THE PLAYER', player)
                    print('game over')
                    go_on_shooting = False
                    exit()
            else:
                print('You missed, now the turn of your rival')
                go_on_shooting = False
        except:
            print('Input typo or out of field, try again')

def main():
    boards = [[[0 for j in range(10)]for i in range(10)],[[0 for j in range(10)]for i in range(10)]]
    set_ships(count, size, boards[0],'ONE')
    set_ships(count, size, boards[1],'TWO')
    while True:
        shoot(boards[1],'ONE')
        game_over(boards[0])
        shoot(boards[0],'TWO')
        game_over(boards[1])

main()

# перенес определение игрока и переход хода в shooting_function, потренировался передавать туда из
# main() номер игрока.
# отловил, что раньше стрелял по собстевнному полю. теперь всё правильно.

# если победил один из игроков, выполняется else на строке 56. Не получается присвоить go_on_shooting = False
# и начинается бесконечный цикл, печатающий print('Input typo or out of field, try again')
# как мне на этом этапе прервать цикл?

# по переходу на ООП мысли следующие:
# классы:
# 1. boards, дочерний board
# methods:
# board_size
# game_over
# print_board
# 2. commands
# methods:
# set_ships
# shoot
# main
# вот если с классом boards чуть более понятно, то с commands не очень понятно
# логика была такая: кто делает (commands) с чем делает (boards). верно ли это?
# как ещё можно структурировать этот вопрос?
