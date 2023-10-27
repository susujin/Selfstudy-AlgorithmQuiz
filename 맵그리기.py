#초기맵 만들기
the_board = {}
for i in range(1,10):
    the_board[i] = ' '

#맵 그리기
def print_board(board):
    for k,v in board.items():
        if k % 3 == 0 and k != 9:
            print("\n" + "-" * 10)
        elif k == 9:
            print()
        else:
            print(v, "| ", end="")

print_board(the_board)