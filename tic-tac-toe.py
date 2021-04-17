Board = {'topLeft' : ' ' , 'topMiddle' : ' ' , 'topRight' : ' ',
         'midLeft' : ' ' , 'midMiddle' : ' ' , 'midRight' : ' ',
         'botLeft' : ' ' , 'botMiddle' : ' ' , 'botRight' : ' '}
def printBoard(board):
    print(board['topLeft'] + '|' + board['topMiddle'] + '|' + board['topRight'])
    print('-+-+-')
    print(board['midLeft'] + '|' + board['midMiddle'] + '|' + board['midRight'])
    print('-+-+-')
    print(board['botLeft'] + '|' + board['botMiddle'] + '|' + board['botRight'])

turn = 'X'
for i in range(9):
    printBoard(Board)
    print('Turn for ' + turn + '. Where do you want to put your ' + turn + '?')
    move = input()
    Board[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
    
       
printBoard(Board)
