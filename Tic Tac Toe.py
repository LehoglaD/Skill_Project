'''Создаем игровое поле'''
board = list(range(1,10))
def draw_board():
    print('-'* 13)
    for i in range(3):
        print('|', board[i*3], "|", board[1+i*3],"|", board[2+i*3], '|')
        print('-' * 13)

'''Принимаем значение от игроков'''
def input_valve_players(current_player):
    valid = False
    while not valid:
        numbers = list(map(str, [1,2,3,4,5,6,7,8,9])) #Список чисел для проверки введенного значения
        player_input = (input('Куда ставим ' + current_player + '?: '))




        if player_input in numbers: #Проверка введено ли число, если да, то преобразовываем в int
            player_input = int(player_input)
        else:
            print('Некорректный ввод. Ведите число от 1 до 9')
            continue
        if str(board[player_input - 1]) in 'X0':
             print('Ошибка! Клетка занята. Введите другое значение')
             continue
        else:
            board[player_input - 1] = current_player #Ставим крестик или нолик, на место выбранное игроком
            valid = True

def check_win(board): #Проверка выиграл ли игрок
    win_situation = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                     (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) # все выигрышные коомбинации
    for i in win_situation:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

'''Основаня функция с игрой'''
def mine_game(board):
    print('Добро пожаловать в крестики-нолики!')
    step = 0 # Переменная для подсчета ходов и смены между 'X' и '0'
    win = False
    while not win:
        draw_board()
        if step % 2 == 0:
            input_valve_players('X')
        else:
            input_valve_players('0')
        step += 1
        winner = check_win(board)
        if step == 9 and not winner:
            draw_board()
            print('Ничья! Спасибо за игру!')
            win = True
        if winner:
            draw_board()
            print(f'Поздравляем! Победил {winner}')
            win = True
mine_game(board)







