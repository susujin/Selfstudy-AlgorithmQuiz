#틱택토(Tic Tac Toe)
import re, random

#초기맵 만들기
the_board = {}
for i in range(1,10):
    the_board[i] = ' '

#맵 그리기
def print_board(board):
    for k,v in board.items():
        print(v, "| ", end="")
        if k % 3 == 0:
            print("\n" + "-" * 10)

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

#빈 맵 출력
print_board(the_board) 
#O/X
turn = 'O' 
#9번까지만 실행 가능해야하며 컴퓨터가 랜덤으로 값을 뽑기위한 리스트, 1~9까지 숫자 중 이미 사용된 숫자는 제거됨
num_list = [i for i in range(1,10)] 

while True: #num_list가 0이상이면 반복
    if turn == 'O': #사용자 입력을 받는 경우
        while True:
            try: #int로 묶어서 문자가 들어오면 무조건 오류발생. 때문에 예외처리함
                print('어느 위치에 표시하시겠습니까? > ')
                space = int(input())
                break
            except:
                print("숫자를 입력해주세요.")

        #정규식 사용((1~9)사이의 숫자인지 확인), 입력된 위치가 비어있는지 확인
        if not re.match('^[1-9]{1}$', str(space)):
            print('(1~9) 숫자 중 입력해주세요.')
            continue
        if not the_board[space] == ' ':
            print('그 자리는 표시할 수 없습니다.')
            continue
    else: #랜덤으로 입력을 받는 경우, 남아있는 숫자 중 랜덤으로 선택
        print("컴퓨터의 랜덤 입력입니다.")
        space = random.choice(num_list)

    #맵에 체크표시 남기고, 해당 위치 값을 num_list에서 지우기
    the_board[space] = turn
    num_list.remove(space)
        
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