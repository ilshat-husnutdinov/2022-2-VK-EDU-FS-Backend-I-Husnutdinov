"""
Игра крестики-нолики
"""


class TicTacGame:
    """
    Класс игры крестики-нолики
    """
    def __init__(self):
        """
        Конструктор класса, создает поле игры и доступные команды игрока
        """
        self.board = [[i] for i in range(1, 10)]
        self.allowed_commands = list(range(1, 10))
        self.player_1 = None
        self.player_2 = None
        self.action = None
        self.current_player = None

    def create_players(self):
        """
        Функция создаёт игроков для объекта класса,
        определяет для них соответствующие действия ( X или 0 ) при изменении поля игры
        и создает текущего игрока, который будет изменяться с каждым ходом игры
        """
        self.player_1 = input('Игрок 1, введите своё имя: ').capitalize()
        while self.player_1.strip() == '':
            self.player_1 = input('Игрок 1, пустой ввод запрещён,введите своё имя: ').capitalize()
        self.player_2 = input('Игрок 2, введите своё имя: ').capitalize()
        while self.player_2.strip() == '':
            self.player_2 = input('Игрок 2, пустой ввод запрещён,введите своё имя: ').capitalize()
        while self.player_1 == self.player_2:
            self.player_2 = input(f'Игрок 2, введите имя, '
                                  f'отличное от имени --> {self.player_1}: ').capitalize()
        self.action = {self.player_1: ' X ', self.player_2: ' 0 '}
        self.current_player = self.player_1

    def swap_player(self, current_player, player_1, player_2):
        """
        Функция принимает на вход аргументы current_player (текущий игрок), player_1 (Игрок 1) и
        player_2 (Игрок 2), при этом current_player равен player_1 или player_2
        Функция возвращает player_2 , если current_player == player_1, иначе вернет player_1
        """
        if current_player not in (player_1, player_2):
            raise ValueError('В функцию переданы некорректные аргументы')
        if current_player == player_1:
            return player_2
        return player_1

    def show_board(self):
        """
        Функция печатает в консоль актуальное поле игры
        """
        print(
            f' —— —— —— —— —— —— \n'
            f'| {self.board[0]} | {self.board[1]} | {self.board[2]} |\n'
            f'|—— ——|—— ——|—— ——|\n'
            f'| {self.board[3]} | {self.board[4]} | {self.board[5]} |\n'
            f'|—— ——|—— ——|—— ——|\n'
            f'| {self.board[6]} | {self.board[7]} | {self.board[8]} |\n'
            f' —— —— —— —— —— —— \n'
        )

    def player_input(self):
        """
        Функция выполняет и возвращает пользовательский ввод игрока.
        Если пользователем вводится НЕцифра, то вызовется ошибка ValueError,
        которая будет обработана, после чего функция вернет False
        """
        try:
            player_step = int(input(f'Ходит: {self.current_player}\n'
                                    f'Для заполнения клетки, введите одну из цифр,'
                                    f' находящихся в квадратных скобках: '))
            return player_step
        except ValueError:
            return False

    def validate_input(self, allowed_commands, command):
        """
        На вход функции передаются аргументы allowed_commands (доступные команды),
        command (команда).
        Если command находится среди allowed_commands, то вернется True, иначе False
        """
        if command in allowed_commands:
            return True
        return False

    def start_game(self):
        """
        Данная функция начинает игру и в цикле выполняет
        команды игроков по заполнению клеток до момента
        выйгрыша одного из игроков
        """
        while self.check_winner() is not True and len(self.allowed_commands) != 0:
            print('-' * 80)
            self.show_board()
            input_player = self.player_input()
            if not self.validate_input(self.allowed_commands, input_player):
                print('-'*80)
                print(f'{self.current_player},'
                      f' Вы ввели некорректный символ, будьте внимательны.'.upper())
                continue
            self.allowed_commands.remove(input_player)
            self.board[input_player - 1] = self.action[self.current_player]
            self.current_player = self.swap_player(self.current_player,
                                                   self.player_1, self.player_2)

        if self.check_winner():
            self.current_player = self.swap_player(self.current_player,
                                                   self.player_1, self.player_2)
            self.show_board()
            print(f'Победил игрок с именем {self.current_player}')
        else:
            self.show_board()
            print('Ничья!')

    def check_winner(self):
        """
        функция возвращает True, если победитель имеется, иначе возвращает False
        """
        for i in range(0, 7, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2]:
                return True
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6]:
                return True
        if self.board[0] == self.board[4] == self.board[8]:
            return True
        if self.board[2] == self.board[4] == self.board[6]:
            return True
        return False


if __name__ == '__main__':
    game = TicTacGame()
    game.create_players()
    game.start_game()
