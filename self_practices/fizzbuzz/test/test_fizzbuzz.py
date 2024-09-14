from fizzbuzz import NumberProcessor, ActionRules, Generator

"""
# Tests for Fizz-Buzz Program

## Requirements

- [x] The program should print numbers from 1 to 100
- [x] For multiples of three, print "Fizz" instead of the number
- [x] For the multiples of five, print "Buzz" instead of the number
- [x] For numbers which are multiples of both three and five, print "FizzBuzz" instead of the number
- [x] For numbers which contain 3, print "Fizz" instead of the number
- [x] For numbers which contain 5, print "Buzz" instead of the number
- [x] For numbers which contain 3 and 5, print "FizzBuzz" instead of the number
"""

processor = NumberProcessor(ActionRules())
generator = Generator(processor)

class TestFizzBuzz:
    def test_should_print_numbers_from_1_to_100_with_replacement_on_certain_numbers(self):
        actual = generator.generate()
        assert actual == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
                          "11", "Fizz", "Fizz", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz",
                          "Fizz", "22", "Fizz", "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz", "Fizz",
                          "Fizz", "Fizz", "Fizz", "FizzBuzz", "Fizz", "Fizz", "Fizz", "Fizz", "Buzz",
                          "41", "Fizz", "Fizz", "44", "FizzBuzz", "46", "47", "Fizz", "49", "Buzz",
                          "FizzBuzz", "Buzz", "FizzBuzz", "FizzBuzz", "Buzz", "Buzz", "FizzBuzz", "Buzz", "Buzz",
                          "FizzBuzz",
                          "61", "62", "Fizz", "64", "Buzz", "Fizz", "67", "68", "Fizz", "Buzz",
                          "71", "Fizz", "Fizz", "74", "FizzBuzz", "76", "77", "Fizz", "79", "Buzz",
                          "Fizz", "82", "Fizz", "Fizz", "Buzz", "86", "Fizz", "88", "89", "FizzBuzz",
                          "91", "92", "Fizz", "94", "Buzz", "Fizz", "97", "98", "Fizz", "Buzz"]


class TestNumberProcessor:
    def test_should_print_fizz_for_multiples_of_three(self):
        actual = processor.process_number(3)
        assert actual == "Fizz"

    def test_should_print_buzz_for_multiples_of_five(self):
        actual = processor.process_number(5)
        assert actual == "Buzz"

    def test_should_print_fizzbuzz_for_multiples_of_three_and_five(self):
        actual = processor.process_number(15)
        assert actual == "FizzBuzz"

    def test_should_print_fizz_when_number_contains_3(self):
        actual = processor.process_number(13)
        assert actual == "Fizz"

    def test_should_print_buzz_when_number_contains_5(self):
        actual = processor.process_number(52)
        assert actual == "Buzz"

    def test_should_print_fizzbuzz_when_number_contains_3_and_5(self):
        actual = processor.process_number(53)
        assert actual == "FizzBuzz"

    def test_should_print_number_when_it_does_not_match_any_rule(self):
        actual = processor.process_number(2)
        assert actual == "2"
