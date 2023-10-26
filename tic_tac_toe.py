import random  
import os 

class TicTacToe:
    def __init__(self) -> None:
        self.reset()

    def print_board(self):
        print("   0   1   2")
        print("0 " +" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("  -----------")
        print("1 " + " " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("  -----------")
        print("2 " + " " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

    def reset(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.done = ""
    
    def check_win_or_draw(self):
        dict_win = {}

        for i in ["X", "O"]:
            #Horizontal
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]

            #Vertical
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]
    
            #Diagonal
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]
    
        if dict_win["X"]:
            self.done = "X"
            print("X venceu!")
        elif dict_win["O"]:
            self.done = "O"
            print("O venceu!")

        c = 0
        for i in range(3):
            for j in range(3):
                 if self.board[i][j] != " ":
                      c += 1
                      break
        
        if c == 0:
            self.done = "d"
            print("Deu empare!")
            return

    def get_player_move(self):
        invalid_mode=True

        while invalid_mode:
            try:
                print("Digite a linha do seu proximo lance:")
                x = int(input())

                print("Digite a coluna do seu proximo lance:")
                y = int(input())

                if self.board[x][y] != " ":
                    print("Posição já preenchida.")
                    continue
            except Exception as e:
                print(e)
                continue

            invalid_mode = False
        self.board[x][y] = "X"

    def make_move(self):
        list_move = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_move.append((i, j))
            
        if len(list_move) > 0:
            x, y = random.choice(list_move)
            self.board[x][y] = "O"



tic_tac_toe = TicTacToe()
tic_tac_toe.print_board()
next = 0

while next == 0:
    os.system("clear")
    tic_tac_toe.print_board()
    while tic_tac_toe.done =="":
        tic_tac_toe.get_player_move()
        tic_tac_toe.make_move()
        os.system("clear")
        tic_tac_toe.print_board()
        tic_tac_toe.check_win_or_draw()
    
    print("Digite 1 para sair do jogo ou qualquer tecla para jogar novamente.")

    next = int(input())
    if next == 1:
        break
    else:
        tic_tac_toe.reset()
        next = 0