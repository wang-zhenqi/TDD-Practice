import pytest

from OptionParserFactory import OptionParserFactory

"""
- BooleanOptionParser
    - Sad Path
        - `my_app -l 1`
        - `my_app -l 2 x`
"""


class TestBooleanOptionParser:
    @pytest.mark.parametrize(["index", "argument_list"], [
        [0, ["-l", "1"]],
        [0, ["-l", "2", "x"]],
    ])
    def test_should_raise_exception_when_it_passes_any_argument(self, index, argument_list):
        with pytest.raises(TypeError):
            boolean_option_parser = OptionParserFactory().get_parser_by_option_type(bool)
            boolean_option_parser.parse(index, argument_list)
