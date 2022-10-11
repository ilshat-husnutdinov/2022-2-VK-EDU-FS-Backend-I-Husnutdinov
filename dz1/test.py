'''
Тесты для игры крестики-нолики
'''
import unittest
import game_after_pylint


class MyTestCase(unittest.TestCase):
    '''
    Тесты для основных функций класса TicTacGame
    '''
    def setUp(self):
        self.game = game_after_pylint.TicTacGame()

    def test_swap(self):
        '''
        Тест для функции, сменяющую игроков местами
        '''
        self.assertEqual(self.game.swap_player('1', '2', '1'), '2')  # add assertion here
        self.assertEqual(self.game.swap_player('2', '2', '1'), '1')

        with self.assertRaises(ValueError) as exc:
            self.game.swap_player('1', '2', '3')
        self.assertEqual('В функцию переданы некорректные аргументы', exc.exception.args[0])

    def test_validate_input(self):
        '''
        Тест для функции, проверяющей корректность ввода игроком разрешенной команды
        '''
        self.assertEqual(self.game.validate_input([1, 2, 3, 4, 5], 2), True)
        self.assertEqual(self.game.validate_input(['Up', 'Down', 'Left', 'Right'], 'Left'), True)
        self.assertEqual(self.game.validate_input([1, 2, 3, 4, 5], 0), False)
        self.assertEqual(self.game.validate_input(['Up', 'Down', 'Left', 'Right'], 'Corner'), False)


if __name__ == '__main__':
    unittest.main()
