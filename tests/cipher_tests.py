from unittest import TestCase, main
from main import caesar


class test_cipher(TestCase):

    def test_spaces_and_other_characters_between_words(self):
        self.assertEqual(caesar("chill and relax", 12, "encode"), "otuxx mzp dqxmj")
        self.assertEqual(caesar("right%of%the%bat", 25, "encode"), "qhfgs%ne%sgd%azs")

    def test_letter_case_transformation(self):
        self.assertEqual(caesar("DiFfEreNt", 14, "encode"), "rwttsfsbh")

    def test_up_to_26_letters_encoding(self):
        self.assertEqual(caesar("hello", 17, "encode"), "yvccf")

    def test_up_to_26_letters_decoding(self):
        self.assertEqual(caesar("lio", 10, "decode"), "bye")

    def test_outside_26_letters_encoding(self):
        self.assertEqual(caesar("extraterrestrial", 57, "encode"), "jcywfyjwwjxywnfq")

    def test_outside_26_letters_decoding(self):
        self.assertEqual(caesar("dwnno", 40, "decode"), "pizza")

    def test_start_text_type_error(self):
        with self.assertRaises(TypeError):
            caesar(21313, 23, "encode")

    def test_shift_amount_type_error(self):
        with self.assertRaises(TypeError):
            caesar("sustainability", "$#@@!", "encode")

    def test_cipher_direction_value_error(self):
        with self.assertRaises(ValueError):
            caesar("heritage", 12, "turnleft")


if __name__ == '__main__':
    main()
