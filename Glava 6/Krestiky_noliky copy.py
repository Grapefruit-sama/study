# Программа "Крестики-нолики"
# Компьютер играет против пользователя

# глобальные константы
X = 'x'
O = 'O'
EMPTY = ''
TIE = 'Ничья'
NUM_SQUARES = 9


def display_instruct():
    """Выводит на экран инструкцию для игрока"""
    print(
        '''
        Добро пожаловать на ринг грандеознейших
        интелектуальных состязаний всех времен.
        Твой мозг и мой процессор сойдуться в 
        схватке за доской игры "Крестики-нолики"

        Чтобы сделать ход, введи число от 0 до 8.
        Числа однозначно соответствуют полям доски -
        так как показано ниже:
         0 | 1 | 2
        -----------
         3 | 4 | 5
        -----------
         6 | 7 | 8
        Приготовься к бою, кожанный ублюдок. Вот-вот
        начнется решающее сражение.\n'''
    )


def ask_yes_no(question):
    """Задает вопрос с ответом "Да" или "Нет"."""
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Просит ввести число из диапазона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Определяет пренадлежность первого хода"""
    go_first = ask_yes_no('Хочешь оставить за собой первый ход? (y/n): ')
    if go_first == 'y':
        print('\nну чтож, даю тебе фору: играй крестиками')
        human = X
        computer = O
    else:
        print('\nТвоя удаль тебя пошубит... Буду начинать я')
        computer = X
        human = O
    return computer, human


def new_board():
    """Создает новую игровую доску"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображает игровую доску на экране"""
    print(f'\n\t {board[0]} | {board[1]} | {board[2]}')
    print('\t', '---------')
    print(f'\n\t {board[3]} | {board[4]} | {board[5]}')
    print('\t', '---------')
    print(f'\n\t {board[6]} | {board[7]} | {board[8]}\n')


def legal_moves(board):
    """Создает список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определяет победителя в игре"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    """Получае ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей (0:8)", 0, NUM_SQUARES)
        if move not in legal:
            print('\nСмешной человек! Это поле уже занято. Выбери другое!\n')
        print('Ладно...')
    return move


def computer_move(board, computer, human):
    """Делает ход за компьютерного противника"""
    # Создадим рабочую копию доски, потому что функция будет менять значения в списке
    board = board[:]
    # поля от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print('Я выберу поле номер', end='')
    for move in legal_moves(board):
        board[move] = computer
    # если следующим ходом может победить компьютер выберем этот ход
        if winner(board) == computer:
            print(move)
            return move
        # Выполнив проверку отменим внесенные изменения
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # выполнив проверку отменим внесенные изменения
        board[move] = EMPTY
    # Поскольку следующим ходом ни одна сторона не может победить
    # выберем лучшее из доступных полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Осуществляет переод хода"""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя игры"""
    if the_winner != TIE:
        print(f'Три {the_winner} в ряд!\n')
    else:
        print('Ничья!')
    if the_winner == computer:
        print('Как я и предсказывал победа за мной')
    elif the_winner == human:
        print('Этого не может быть!! Как это возможно?!?!?')
        print('В следубщий раз я этого не допущу')
    elif the_winner == TIE:
        print('То что это ничья - просто твое везение')


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()
input('\n\nНажмите Enter чтобы выйти')
