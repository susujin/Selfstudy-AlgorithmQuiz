#틱택토

import random

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
num_list = [i for i in range(1,10)] #9번까지만 실행 가능해야하기에 만든 리스트, 1~9까지 숫자 중 이미 사용된 숫자는 제거됨

while len(num_list) > 0: #num_list가 0이상이면 반복
    while True:
        print('어느 위치에 표시하시겠습니까? > ')
        if turn == 'O': #사용자 입력을 받는 경우
            space = int(input())
        else: #랜덤으로 입력을 받는 경우, 남아있는 숫자 중 랜덤으로 선택
            space = random.choice(num_list)

        #입력된 값이 비어있을 경우 표시 후 num_list에서 해당 숫자 제거
        if the_board[space] == ' ':
            the_board[space] = turn
            num_list.remove(space)
            break
        #입력된 값이 비어있지 않은 경우
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
        if len(num_list) == 0:
            print('무승부 입니다.')
            print('게임이 종료되었습니다.')
            break

    