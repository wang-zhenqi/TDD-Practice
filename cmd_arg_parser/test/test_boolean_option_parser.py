import pytest

from Exceptions.TooManyArgumentsException import TooManyArgumentsException
from Parsers.OptionParserFactory import OptionParserFactory
from my_app import Options

"""
- Happy Path
    - single argument with single values
        - `my_app -l`
- Sad Path
    - `my_app -l 1`
    - `my_app -l 2 x`
"""


@pytest.fixture
def boolean_option_parser():
    return OptionParserFactory().get_parser_by_option_type(bool)


class TestBooleanOptionParser:
    def test_single_argument_with_single_boolean_values(self, boolean_option_parser):
        actual = boolean_option_parser.parse(["-l"], 0)
        assert actual

    @pytest.mark.parametrize(["index", "argument_list"], [
        [0, ["-l", "1"]],
        [0, ["-l", "2", "x"]],
    ])
    def test_should_raise_exception_when_it_passes_any_argument(self, index, argument_list, boolean_option_parser):
        with pytest.raises(TooManyArgumentsException):
            boolean_option_parser.parse(argument_list, index)
