class Board(object):
    def __init__(self, board_size=10, count=1, size=1):
        self.board_size = board_size
        self.count = count
        self.size = size
        self.board = [[0 for j in range(self.board_size)]for i in range(self.board_size)]
        c = 0
        while c < self.count:
            s = 0
            while s < size:
                try:
                    coordinates = list(map(int, input().split()))
                    if self.board[coordinates[0]][coordinates[1]] != 1:
                        self.board[coordinates[0]][coordinates[1]] = 1
                        s += 1
                    else:
                        print('This cell is occupied by existing ship, try again')
                except IndexError:
                    print('Input typo or out of field, try again')
            print('Ship',c+1,'is set')
            c += 1
        self.print_board()

    def print_board(self):
        for i in reversed(self.board):
            print(i)

    def board_is_empty(self):
        sum = 0
        for i in self.board:
            for j in i:
                sum = sum + j
        if sum == 0:
            return True
        else:
            return False
# написать короче

    def get_shoot(self):
        while True:
            try:
                shoot = list(map(int,input().split()))
                if self.board[shoot[0]][shoot[1]] == 1:
                    print('The shoot hit the ship!')
                    self.board[shoot[0]][shoot[1]] = 0
                    if self.board_is_empty() == True:
                        print('game is over')
                        exit()
                else:
                    print('You missed, now the turn of your rival')
                    break
            except IndexError:
                print('Input typo or out of field, try again')

def main():
    board1 = Board()
    board2 = Board()
    while True:
        board2.get_shoot()
        board1.get_shoot()

if __name__ == '__main__':
    main()
