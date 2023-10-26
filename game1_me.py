#틱택토

#초기맵 만들기
the_board = {}
for i in range(1,10):
    the_board[i] = ' '

#맵 그리기
def print_board(board):
    for k,v in board.items():
        print(v, "| ", end="")
        if k % 3 == 0:
            print("\n" + "-" * 9)

#게임종료 확인
#가로/세로/대각선이 같으면서 공백 X
def game_over(board):
    #가로
    for i in range(1,8,3):
        if board[i] == board[i+1] == board[i+2]:
            if board[i] != ' ':
                print(f'승자는 {board[i]}입니다')
                return True
    #세로
    for i in range(1,4):
        if board[i] == board[i+3] == board[i+6]: 
            if board[i] != ' ':
                print(f'승자는 {board[i]}입니다')
                return True
    #대각션
    if board[1] == board[5] == board [9]:
        if board[1] != ' ':
            print(f'승자는 {board[1]}입니다')
            return True 
    if board[3] == board[5] == board [7]:
        if board[3] != ' ':
            print(f'승자는 {board[3]}입니다')
            return True
        
    return False

print_board(the_board) #빈 맵 출력
turn = 'O' #O/X
count = 0 #9번까지만 실행 가능해야하기에 만든 변수

while count < 10: 
    while True:
        print('어느 위치에 표시하시겠습니까? > ')
        space = int(input())

        if the_board[space] == ' ':
            the_board[space] = turn
            count += 1
            break
        else:
            print('그 자리는 표시할 수 없습니다.')

    #맵 그리기
    print_board(the_board)

    #순서 바꾸기
    if turn == 'O':
        turn = 'X'
    else:
        turn = 'O'

    #게임종료 확인하기
    if game_over(the_board) == True:
        print('게임이 종료되었습니다.')
        break
    else:
        if count == 9:
            print('무승부 입니다.')
            print('게임이 종료되었습니다.')
            break

    