from random import shuffle
board_width = 4
board_height = 4
win_board = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,'Empty']]
print('Move the "Empty" around the field to order the numbers from 1 to 15')
print('starting with the top right corner and have the Empty as the last element')
print('in the bottom down corner. Allowed moves: up, down, left, right.')

def beauty_out(board):
    for y in board:
        print '|'.join(map(str, y))
    print ''

def shuffle_board(board):
    #shuffle(board)
    #for y in board:
    #    shuffle([], y)
    pass

def get_blank_position(board):
    for y in range(board_width):
        for x in range(board_height):
            if board[y][x] is 'Empty':
                return (x, y)


def valid_move(board, action, pos_x, pos_y):

    if action is 'UP':
        if pos_y is 0:
            return False
    if action is 'DOWN':
        if pos_y is board_height-1:
            return False
    if action is 'LEFT':
        if pos_x is 0:
            return False
    if action is 'RIGHT':
        if pos_x is board_width-1:
            return False

    return True

def makeMove(board, action):

    pos_x, pos_y = get_blank_position(board)

    if valid_move(board, action, pos_x, pos_y):

        if action is 'UP':
            board[pos_y-1][pos_x], board[pos_y][pos_x] = board[pos_y][pos_x], board[pos_y-1][pos_x]
        if action is 'DOWN':
            board[pos_y+1][pos_x], board[pos_y][pos_x] = board[pos_y][pos_x], board[pos_y+1][pos_x]
        if action is 'LEFT':
            board[pos_y][pos_x-1], board[pos_y][pos_x] = board[pos_y][pos_x], board[pos_y][pos_x-1]
        if action is 'RIGHT':
            board[pos_y][pos_x+1], board[pos_y][pos_x] = board[pos_y][pos_x], board[pos_y][pos_x+1]
        if board == win_board:
            print''
            print('VICTORY!')
            quit()
    else:
        print('Your move is out of border')
        print('Try one more time')
        print ''
    return board


def main():

    board = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,'Empty',15]]
    shuffle_board(board)
    beauty_out(board)

    while True:
        print('your move...')

        cmd = raw_input()
        if cmd.strip() == 'up' or cmd.strip() == 'down' or cmd.strip() == 'right' or cmd.strip() == 'left':
            if cmd.strip() == 'up':
                action = 'UP'
            if cmd.strip() == 'down':
                action = 'DOWN'
            if cmd.strip() == 'left':
                action = 'LEFT'
            if cmd.strip() == 'right':
                action = 'RIGHT'
            board = makeMove(board, action)
            beauty_out(board)
        else:
            print('up, down, left or right please')

        pass


main()