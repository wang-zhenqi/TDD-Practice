import pytest

from Exceptions.InsufficientArgumentException import InsufficientArgumentException
from Exceptions.TooManyArgumentsException import TooManyArgumentsException
from OptionParser import OptionParser
from Options.Options import available_options

"""
- Happy Path
    - single argument with single values
        - `my_app -l`
        - `my_app -p 8080`
        - `my_app -d /some/path`
- Sad Path
    - `my_app -l 1`
    - `my_app -l 2 x`
    - `my_app -p 8080 8090`
    - `my_app -d`
    - `my_app -l -d`
    - `my_app -d -l`
    - `my_app -p abcd`
"""


@pytest.fixture
def boolean_option_parser():
    return OptionParser(available_options.logging)


@pytest.fixture
def integer_option_parser():
    return OptionParser(available_options.port)


@pytest.fixture
def string_option_parser():
    return OptionParser(available_options.directory)


class TestBooleanOptionParser:
    def test_single_argument_with_single_boolean_value(self, boolean_option_parser):
        actual = boolean_option_parser.parse(["-l"], 0)
        assert actual

    @pytest.mark.parametrize(["index", "argument_list"], [
        [0, ["-l", "1"]],
        [0, ["-l", "2", "x"]],
    ])
    def test_should_raise_exception_when_it_passes_any_argument(self, index, argument_list, boolean_option_parser):
        with pytest.raises(TooManyArgumentsException):
            boolean_option_parser.parse(argument_list, index)


class TestSingleValuedOptionParser:
    def test_single_argument_with_single_integer_value(self, integer_option_parser):
        assert 8080 == integer_option_parser.parse(["-p", "8080"], 0)

    def test_single_argument_with_single_string_value(self, string_option_parser):
        assert "/some/path" == string_option_parser.parse(["-d", "/some/path"], 0)

    def test_should_raise_exception_when_more_than_one_value_given(self, string_option_parser):
        with pytest.raises(TooManyArgumentsException):
            string_option_parser.parse(["-p", "8080", "8090"], 0)

    @pytest.mark.parametrize("argument_list",
                             [["-d"], ["-l", "-p"], ["-d", "-l"]])
    def test_should_raise_exception_when_no_arguments_given(self, argument_list, string_option_parser):
        with pytest.raises(InsufficientArgumentException):
            string_option_parser.parse(argument_list, 0)

    @pytest.mark.parametrize("argument_list",
                             [["-p", "abcd"]])
    def test_should_raise_exception_when_argument_type_is_not_match(self, argument_list, integer_option_parser):
        with pytest.raises(ValueError):
            integer_option_parser.parse(argument_list, 0)
class TestMultipleValuedOptionParser:
    @pytest.mark.parametrize(["argument_list", "expected_values"],
                             [
                                 [["-d", "1", "2"], [1, 2]],
                                 [["-d", "-1", "-2", "3"], [-1, -2, 3]],
                             ])
    def test_multiple_arguments_with_multiple_integer_values(self, argument_list, expected_values):
        parser = OptionParser(available_options.digits)
        assert expected_values == parser.parse(argument_list, 0)
