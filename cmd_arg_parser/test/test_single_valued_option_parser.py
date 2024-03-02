import pytest

from Exceptions.NotSufficientArgumentException import NotSufficientArgumentException
from Exceptions.TooManyArgumentsException import TooManyArgumentsException
from Parsers.SingleValuedOptionParser import SingleValuedOptionParser

"""
- Sad Path
    - SingleValuedOptionParser
        - `my_app -p 8080 8090`
        - `my_app -d`
        - `my_app -l -d`
        - `my_app -d -l`
        - `my_app -p abcd`
"""


class TestSingleValuedOptionParser:
    def test_should_raise_exception_when_more_than_one_value_given(self):
        with pytest.raises(TooManyArgumentsException):
            parser = SingleValuedOptionParser(lambda x: x)
            parser.parse(0, ["-p", "8080", "8090"])

    @pytest.mark.parametrize("argument_list",
                             [["-d"], ["-l", "-p"], ["-d", "-l"]])
    def test_should_raise_exception_when_no_arguments_given(self, argument_list):
        with pytest.raises(NotSufficientArgumentException):
            parser = SingleValuedOptionParser(lambda x: x)
            parser.parse(0, argument_list)

    @pytest.mark.parametrize("argument_list",
                             [["-p", "abcd"]])
    def test_should_raise_exception_when_argument_type_is_not_match(self, argument_list):
        with pytest.raises(ValueError):
            parser = SingleValuedOptionParser(int)
            parser.parse(0, argument_list)
