import unittest
from game_layer import Game


class TestGame(unittest.TestCase):
    def test_with_one_letter(self):
        game = Game("a1b2c3d4", "BANAS")
        game.fill_guessing_word_with_special_char()
        game.accept_letter_for_game("B")
        lifes_count = game.get_lifes_count()
        word = game.get_word()
        guessing_word = game.get_guessing_word()
        game_status = game.get_game_status()
        incorrect_letters = game.get_incorrect_guesed_letters()
        letters_left = game.get_left_letters()
        self.assertEqual(lifes_count, 10)
        self.assertEqual(word, "BANAS")
        self.assertEqual(guessing_word, ["B", "_", "_", "_", "_"])
        self.assertEqual(game_status, False)
        self.assertEqual(incorrect_letters, [])
        self.assertEquals(
            letters_left,
            [
                "A",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
                "Z",
            ],
        )

    def test_with_two_letters(self):
        game = Game("a1b2c3d4", "BANAS")
        game.fill_guessing_word_with_special_char()
        game.accept_letter_for_game("B")
        game.accept_letter_for_game("A")
        lifes_count = game.get_lifes_count()
        word = game.get_word()
        guessing_word = game.get_guessing_word()
        game_status = game.get_game_status()
        incorrect_letters = game.get_incorrect_guesed_letters()
        letters_left = game.get_left_letters()
        self.assertEqual(lifes_count, 10)
        self.assertEqual(word, "BANAS")
        self.assertEqual(guessing_word, ["B", "A", "_", "A", "_"])
        self.assertEqual(game_status, False)
        self.assertEqual(incorrect_letters, [])
        self.assertEquals(
            letters_left,
            [
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
                "Z",
            ],
        )

    def test_with_three_letters(self):
        game = Game("a1b2c3d4", "BANAS")
        game.fill_guessing_word_with_special_char()
        game.accept_letter_for_game("B")
        game.accept_letter_for_game("A")
        game.accept_letter_for_game("Z")
        lifes_count = game.get_lifes_count()
        word = game.get_word()
        guessing_word = game.get_guessing_word()
        game_status = game.get_game_status()
        incorrect_letters = game.get_incorrect_guesed_letters()
        letters_left = game.get_left_letters()
        self.assertEqual(lifes_count, 9)
        self.assertEqual(word, "BANAS")
        self.assertEqual(guessing_word, ["B", "A", "_", "A", "_"])
        self.assertEqual(game_status, False)
        self.assertEqual(incorrect_letters, ["Z"])
        self.assertEquals(
            letters_left,
            [
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
            ],
        )

    def test_with_three_letters(self):
        game = Game("a1b2c3d4", "BANAS")
        game.fill_guessing_word_with_special_char()
        game.accept_letter_for_game("B")
        game.accept_letter_for_game("A")
        game.accept_letter_for_game("Z")
        game.accept_letter_for_game("J")
        lifes_count = game.get_lifes_count()
        word = game.get_word()
        guessing_word = game.get_guessing_word()
        game_status = game.get_game_status()
        incorrect_letters = game.get_incorrect_guesed_letters()
        letters_left = game.get_left_letters()
        self.assertEqual(lifes_count, 8)
        self.assertEqual(word, "BANAS")
        self.assertEqual(guessing_word, ["B", "A", "_", "A", "_"])
        self.assertEqual(game_status, False)
        self.assertEqual(incorrect_letters, ["Z", "J"])
        self.assertEquals(
            letters_left,
            [
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
            ],
        )

    def test_win_game(self):
        game = Game("a1b2c3d4", "BANAS")
        game.fill_guessing_word_with_special_char()
        game.accept_letter_for_game("B")
        game.accept_letter_for_game("A")
        game.accept_letter_for_game("Z")
        game.accept_letter_for_game("J")
        game.accept_letter_for_game("N")
        game.accept_letter_for_game("S")
        lifes_count = game.get_lifes_count()
        word = game.get_word()
        guessing_word = game.get_guessing_word()
        game_status = game.get_game_status()
        incorrect_letters = game.get_incorrect_guesed_letters()
        letters_left = game.get_left_letters()
        self.assertEqual(lifes_count, 8)
        self.assertEqual(word, "BANAS")
        self.assertEqual(guessing_word, ["B", "A", "N", "A", "S"])
        self.assertEqual(game_status, True)
        self.assertEqual(incorrect_letters, ["Z", "J"])
        self.assertEquals(
            letters_left,
            [
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "K",
                "L",
                "M",
                "O",
                "P",
                "Q",
                "R",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
            ],
        )

    def test_win_game(self):
        game = Game("a1b2c3d4", "BANAS")
        game.fill_guessing_word_with_special_char()
        game.accept_letter_for_game("B")
        game.accept_letter_for_game("A")
        game.accept_letter_for_game("Z")
        game.accept_letter_for_game("J")
        game.accept_letter_for_game("N")
        game.accept_letter_for_game("X")
        game.accept_letter_for_game("W")
        game.accept_letter_for_game("P")
        game.accept_letter_for_game("C")
        game.accept_letter_for_game("D")
        game.accept_letter_for_game("E")
        game.accept_letter_for_game("M")
        game.accept_letter_for_game("L")
        lifes_count = game.get_lifes_count()
        word = game.get_word()
        guessing_word = game.get_guessing_word()
        game_status = game.get_game_status()
        incorrect_letters = game.get_incorrect_guesed_letters()
        letters_left = game.get_left_letters()
        self.assertEqual(lifes_count, 0)
        self.assertEqual(word, "BANAS")
        self.assertEqual(guessing_word, ["B", "A", "N", "A", "_"])
        self.assertEqual(game_status, False)
        self.assertEqual(
            incorrect_letters,
            ["Z", "J", "X", "W", "P", "C", "D", "E", "M", "L"],
        )
        self.assertEquals(
            letters_left,
            [
                "F",
                "G",
                "H",
                "I",
                "K",
                "O",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "Y",
            ],
        )


if __name__ == "__main__":
    unittest.main()
